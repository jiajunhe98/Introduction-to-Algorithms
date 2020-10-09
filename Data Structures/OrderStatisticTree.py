import  RedBlackTree

class OrderStatisticsTree(RedBlackTree.RedBlackTree):
    """
    A class to implement Order Statistics Tree

    This tree is an extension of Red Black Tree, it takes a list of value with or without satellite data.
    Besides having all the properties of RB Tree, it can find the rank of an given node, or select out the k-th node
    in O(lgn) time.

    Args:
        list(list): list of data
        satellite_data(bool): if the entries in the list contain satellite data

    Attributes:
        root: a ptr to the root node
        null_node: a pseudo node represents the parent of root node and the children of leaf nodes

    """
    def __init__(self, list, satellite = None):
        list2 = []
        if satellite == None:
            for i in list:
                list2.append([i, [0]])
        else:
            for i in list:
                list2.append([i[0],[0,[i[1]]]])
        self.satellite = satellite
        self.null_node = RedBlackTree.Node(None)
        self.null_node.color = "BLACK"
        self.null_node.satellite_data = [0]
        self.root = self.null_node
        for i in list2:
            self.insert(i[0],i[1])

    def left_rotate(self, current_node: RedBlackTree.Node):
        """left rotate"""
        super().left_rotate(current_node)
        current_node.parent.satellite_data[0] = current_node.satellite_data[0]
        current_node.satellite_data[0] = current_node.left.satellite_data[0]\
                                         + current_node.right.satellite_data[0] + 1

    def right_rotate(self, current_node: RedBlackTree.Node):
        """right rotate"""
        super().right_rotate(current_node)
        current_node.parent.satellite_data[0] = current_node.satellite_data[0]
        current_node.satellite_data[0] = current_node.left.satellite_data[0]\
                                         + current_node.right.satellite_data[0] + 1

    def inorder_walk(self, start_node = None):
        """return a list of all element ordered by inorder-walking"""
        if start_node == None:
            start_node = self.root
        return_list = []
        null_node = self.null_node
        def __inorder_walk(start_node = self.root, nullnode = null_node):
            if start_node == nullnode:
                return 0
            __inorder_walk(start_node.left)
            if self.satellite:
                return_list.append((start_node.key, start_node.satellite_data[1][0]))
            else:
                return_list.append(start_node.key)
            __inorder_walk(start_node.right)

        __inorder_walk(start_node)
        return return_list

    def insert(self, value, satellite_data):
        """insert an element and remain the properties of red black tree"""
        insert_node = RedBlackTree.Node(value,satellite_data)
        current_node = self.root
        last_node = None
        left_right = 0  #to indicate which child the new node should insert in
        while current_node != self.null_node:
            if value <= current_node.key:
                last_node = current_node
                current_node = current_node.left
                left_right = 0
            else:
                last_node = current_node
                current_node = current_node.right
                left_right = 1
        if last_node == None:
            self.root = insert_node
            insert_node.parent = self.null_node
            insert_node.left = self.null_node
            insert_node.right = self.null_node
        else:
            if left_right == 0:
                last_node.left = insert_node
                insert_node.parent = last_node
                insert_node.left = self.null_node
                insert_node.right = self.null_node
            else:
                last_node.right = insert_node
                insert_node.parent = last_node
                insert_node.right = self.null_node
                insert_node.left = self.null_node
        original_insert = insert_node
        while insert_node != self.null_node:
            insert_node.satellite_data[0] += 1
            insert_node = insert_node.parent
        self.insert_fixup(original_insert)

    def insert_fixup(self, current_node: RedBlackTree.Node):
        """fix up the properties of red black tree after insertion"""
        while current_node.parent.color == "RED" and self.root != current_node:
            if current_node.parent.parent.left == current_node.parent:
                if current_node.parent.parent.right.color == "RED":
                    current_node.parent.color = "BLACK"
                    current_node.parent.parent.color = "RED"
                    current_node.parent.parent.right.color = "BLACK"
                    current_node = current_node.parent.parent
                else:
                    if current_node.parent.right == current_node:
                        self.left_rotate(current_node.parent)
                        current_node = current_node.left
                    current_node.parent.color = "BLACK"
                    current_node.parent.parent.color = "RED"
                    self.right_rotate(current_node.parent.parent)
            else:
                if current_node.parent.parent.left.color == "RED":
                    current_node.parent.color = "BLACK"
                    current_node.parent.parent.color = "RED"
                    current_node.parent.parent.left.color = "BLACK"
                    current_node = current_node.parent.parent
                else:
                    if current_node.parent.left == current_node:
                        self.right_rotate(current_node.parent)
                        current_node = current_node.right
                    current_node.parent.color = "BLACK"
                    current_node.parent.parent.color = "RED"
                    self.left_rotate(current_node.parent.parent)
        self.root.color = "BLACK"

    def delete(self, value):
        """delete an element by the value and keep the properties of red black tree"""
        deleted_node = self.search(value)
        if deleted_node == None:
            return 0
        deleted_node_original_color = deleted_node.color
        if deleted_node.right == self.null_node:               #right child is null
            node_to_fix = deleted_node.left
            self.transplant(deleted_node, deleted_node.left)
            del deleted_node
        elif deleted_node.left == self.null_node:              #left child is null
            node_to_fix = deleted_node.right
            self.transplant(deleted_node, deleted_node.right)
            del deleted_node
        else:                                                  #no child is null
            if deleted_node.right.left == self.null_node:      #if the right child has no left child
                node_to_fix = deleted_node.right.right
                node_to_fix.parent = deleted_node.right
                deleted_node_original_color = node_to_fix.color
                self.transplant(deleted_node, deleted_node.right)
                deleted_node.left.parent = node_to_fix.parent
                node_to_fix.parent.left = deleted_node.left
                node_to_fix.parent.color = deleted_node.color
                del deleted_node
            else:
                trans_node = self.minium(deleted_node.right) #if the right child has left child
                deleted_node.key = trans_node.key
                deleted_node.satellite_data = trans_node.satellite_data
                node_to_fix = trans_node.right
                deleted_node_original_color = trans_node.color
                self.transplant(trans_node, trans_node.right)
                del trans_node

        if node_to_fix != self.null_node:
            node_to_fix.satellite_data = node_to_fix.left.satellite_data[0] + node_to_fix.right.satellite_data[0] + 1
        original_node_to_fix = node_to_fix
        while node_to_fix.parent != self.null_node:
            node_to_fix.parent.satellite_data[0] -= 1
            node_to_fix = node_to_fix.parent
        if deleted_node_original_color == "BLACK":
            self.delete_fixup(original_node_to_fix)

    def transplant(self, deleted_node: RedBlackTree.Node, trans_node: RedBlackTree.Node):
        """transplant a node and its subtree to cover another node,
        keep in mind that the child of deleted node has not assigned yet"""
        trans_node.parent = deleted_node.parent
        if deleted_node.parent == self.null_node:
            self.root = trans_node
        else:
            if deleted_node.parent.left == deleted_node:
                deleted_node.parent.left = trans_node
            else:
                deleted_node.parent.right = trans_node

    def delete_fixup(self, deleted_node: RedBlackTree.Node):
        """fix up the properties of Red Black Tree after deletion"""
        while self.root != deleted_node and deleted_node.color == "BLACK":
            if deleted_node == deleted_node.parent.left:
                if deleted_node.parent.right.color == "RED":
                    '''case 1: brother node is RED
                    let's change it to BLACK by rotating'''
                    deleted_node.parent.color = "RED"
                    deleted_node.parent.right.color = "BLACK"
                    self.left_rotate(deleted_node.parent)
                if deleted_node.parent.right.color == "BLACK":
                    '''case 2&3&4: brother node is BLACK
                    let's check its 2 child'''
                    if deleted_node.parent.right.left.color == "BLACK" \
                        and deleted_node.parent.right.right.color == "BLACK":
                        '''case 2: 2 children of brother node are all BLACK
                        Here we need not to check if the brother node is/is not null node
                        because hb(deleted_node) = hb(brother_node), which indicating that brother is not null node'''
                        deleted_node.parent.right.color = "RED"
                        deleted_node = deleted_node.parent
                    else :
                        if deleted_node.parent.right.left.color == "RED":
                            '''case 3: left child of the brother child is RED
                            let's change it to BLACK and change the right child to RED by rotating
                            and after this operation, it will be case 4'''
                            deleted_node.parent.right.left.color = "BLACK"
                            deleted_node.parent.right.color = "RED"
                            self.right_rotate(deleted_node.parent.right)

                        '''case 4: the last case: right child of the brother node is RED
                        In this case,we will fix up all properties of the tree and set the current to root'''
                        deleted_node.parent.right.color = deleted_node.parent.color
                        deleted_node.parent.color = "BLACK"
                        deleted_node.parent.right.right.color = "BLACK"
                        self.left_rotate(deleted_node.parent)
                        deleted_node = self.root
            else:
                '''symmetrical situation'''
                if deleted_node.parent.left.color == "RED":
                    '''case 1: brother node is RED
                    let's change it to BLACK by rotating'''
                    deleted_node.parent.color = "RED"
                    deleted_node.parent.left.color = "BLACK"
                    self.right_rotate(deleted_node.parent)
                if deleted_node.parent.left.color == "BLACK":
                    '''case 2&3&4: brother node is BLACK
                    let's check its 2 child'''
                    if deleted_node.parent.left.right.color == "BLACK" \
                            and deleted_node.parent.left.left.color == "BLACK":
                        '''case 2: 2 children of brother node are all BLACK
                        Here we need not to check if the brother node is/is not null node
                        because hb(deleted_node) = hb(brother_node), which indicating that brother is not null node'''
                        deleted_node.parent.left.color = "RED"
                        deleted_node = deleted_node.parent
                    else:
                        if deleted_node.parent.left.right.color == "RED":
                            '''case 3: right child of the brother child is RED
                            let's change it to BLACK and change the left child to RED by rotating
                            and after this operation, it will be case 4'''
                            deleted_node.parent.left.right.color = "BLACK"
                            deleted_node.parent.left.color = "RED"
                            self.left_rotate(deleted_node.parent.left)

                        '''case 4: the last case: left child of the brother node is RED
                        In this case,we will fix up all properties of the tree and set the current to root'''
                        deleted_node.parent.left.color = deleted_node.parent.color
                        deleted_node.parent.color = "BLACK"
                        deleted_node.parent.left.left.color = "BLACK"
                        self.right_rotate(deleted_node.parent)
                        deleted_node = self.root
        deleted_node.color = "BLACK"

    def select(self,k, start_node = None) -> RedBlackTree.Node:
        """find the kth element in the tree"""
        if k <= 0:
            print("k must be positive")
            return -1
        if k > self.root.satellite_data[0]:
            print("k must be smaller than the size of the tree")
            return -1
        if start_node == None:
            start_node = self.root
        if k == start_node.left.satellite_data[0]+1:
            return start_node
        if k < start_node.left.satellite_data[0]+1:
            return self.select(k,start_node.left)
        else:
            return self.select(k-start_node.left.satellite_data[0]-1,start_node.right)

    def rank(self, given_node: RedBlackTree.Node) ->int:
        """take a node as input, find its rank"""
        r = given_node.left.satellite_data[0] + 1
        parent_node = given_node
        while parent_node != self.null_node:
            if parent_node == parent_node.parent.right:
                r = r + parent_node.parent.left.satellite_data[0] + 1
            parent_node = parent_node.parent
        return r

    def getsubsize(self,node: RedBlackTree.Node) -> int:
        """take a node as input, return the size attribute (size of sub-trees, containing itself) """
        return node.satellite_data[0]





tree = OrderStatisticsTree([11,2,1,7,5,8,14,15])
print(tree.inorder_walk())
#tree.insert(4)
tree.delete(5)
print(tree.inorder_walk())
print(tree.select(6))
print(tree.rank(tree.root))
