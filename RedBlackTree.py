class Node:
    """The node in Red Black Tree"""
    def __init__(self, key, satellite_data = None):
        """initialization"""
        self.key = key
        self.satellite_data = satellite_data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"

class RedBlackTree:
    """implement red black tree to store a list, each node stores a tuple of the index/value and the satellite data"""
    def __init__(self, list, satellite = None):
        """initialization"""
        self.satellite = satellite
        self.null_node = Node(None)
        self.null_node.color = "BLACK"
        self.root = self.null_node
        for i in list:
            if self.satellite:
                self.insert(i[0],i[1])
            else:
                self.insert(i)

    def search(self, key_value) -> Node:
        """search the element by the key"""
        current_node = self.root
        while current_node != self.null_node:
            if key_value == current_node.key:
                return current_node
            elif key_value <= current_node.key:
                current_node =  current_node.left
            else:
                current_node = current_node.right
        return None

    def predecessor(self, current_node: Node) -> Node:
        """return the predecessor of the current node"""
        if current_node.left != self.null_node:
            return self.maxium(current_node.left)
        parent_node = current_node.parent
        while parent_node != self.null_node and parent_node.left == current_node:
            current_node = parent_node
            parent_node = current_node.parent
        if parent_node == self.null_node:
            return None
        return parent_node

    def successor(self, current_node: Node) -> Node:
        """return the successor of the current node"""
        if current_node.right != self.null_node:
            return self.minium(current_node.right)
        parent_node = current_node.parent
        while parent_node != self.null_node and parent_node.right == current_node:
            current_node = parent_node
            parent_node = current_node.parent
        if parent_node == self.null_node:
            return None
        return parent_node

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
                return_list.append((start_node.key, start_node.satellite_data))
            else:
                return_list.append(start_node.key)
            __inorder_walk(start_node.right)

        __inorder_walk(start_node)
        return return_list

    def minium(self, start_node = None) -> Node:
        """return the minium element"""
        if start_node == None:
            start_node = self.root
        if start_node.left == self.null_node:
            return start_node
        else:
            return self.minium(start_node.left)

    def maxium(self, start_node = None) -> Node:
        """return the maxium element"""
        if start_node == None:
            start_node = self.root
        if start_node.right == self.null_node:
            return start_node
        else:
            return self.maxium(start_node.right)

    def left_rotate(self, current_node: Node):
        """left rotate"""
        next_node = current_node.right

        next_node.left.parent = current_node
        current_node.right = next_node.left

        next_node.parent = current_node.parent
        if self.root == current_node:
            self.root = next_node
        elif current_node.parent.left == current_node:
            current_node.parent.left = next_node
        elif current_node.parent.right == current_node:
            current_node.parent.right = next_node

        current_node.parent = next_node
        next_node.left = current_node

    def right_rotate(self, current_node: Node):
        """right rotate"""
        next_node = current_node.left

        next_node.right.parent = current_node
        current_node.left = next_node.right

        next_node.parent = current_node.parent
        if self.root == current_node:
            self.root = next_node
        elif current_node.parent.left == current_node:
            current_node.parent.left = next_node
        elif current_node.parent.right == current_node:
            current_node.parent.right = next_node

        current_node.parent = next_node
        next_node.right = current_node

    def insert(self, value, satellite_data = None):
        """insert an element and remain the properties of red black tree"""
        if self.satellite:
            insert_node = Node(value,satellite_data)
        else:
            insert_node = Node(value)
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
        self.insert_fixup(insert_node)

    def insert_fixup(self, current_node: Node):
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
        if deleted_node_original_color == "BLACK":
            self.delete_fixup(node_to_fix)

    def transplant(self, deleted_node: Node, trans_node: Node):
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

    def delete_fixup(self, deleted_node: Node):
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



tree = RedBlackTree([11,2,1,7,5,8,14,15])
print(tree.inorder_walk())
#tree.insert(4)
tree.delete(5)
print(tree.inorder_walk())




