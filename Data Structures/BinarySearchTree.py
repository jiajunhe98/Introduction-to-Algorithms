class Node:
    """Node in a Binary Search Tree"""
    def __init__(self, key, parent = None, left_child = None, right_child = None):
        """initialization"""
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

class BinarySearchTree:
    """Implement Binary Search Tree"""
    def __init__(self, list):
        """initialization"""
        self.root = Node(list[0])
        if len(list) > 1:
            for i in list[1:]:
                self.insert(i)

    def inorder_tree_walk(self):
        """print elements by inorder walking"""
        if self.root != None:
            self.__inorder_tree_walk__(self.root)
        print("")

    def __inorder_tree_walk__(self,current_node):
        """print elements by inorder walking"""
        if current_node.left_child != None:
            self.__inorder_tree_walk__(current_node.left_child)
        print(current_node.key,end = " ")
        if current_node.right_child != None:
            self.__inorder_tree_walk__(current_node.right_child)

    def preorder_tree_walk(self):
        """print elements by inorder walking"""
        if self.root != None:
            self.__preorder_tree_walk__(self.root)
        print("")

    def __preorder_tree_walk__(self,current_node):
        """print elements by inorder walking"""
        print(current_node.key, end = " ")
        if current_node.left_child != None:
            self.__preorder_tree_walk__(current_node.left_child)
        if current_node.right_child != None:
            self.__preorder_tree_walk__(current_node.right_child)

    def postorder_tree_walk(self):
        """print elements by inorder walking"""
        if self.root != None:
            self.__postorder_tree_walk__(self.root)
        print("")

    def __postorder_tree_walk__(self,current_node):
        """print elements by inorder walking"""
        if current_node.left_child != None:
            self.__postorder_tree_walk__(current_node.left_child)
        if current_node.right_child != None:
            self.__postorder_tree_walk__(current_node.right_child)
        print(current_node.key, end = " ")

    def search(self, key) -> Node:
        """search an element by key, return the object: node"""
        current_node = self.root
        while(current_node != None):
            if current_node.key == key:
                return  current_node
            elif current_node.key >= key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node

    def minimum(self, start_node = None) -> Node:
        """return the minium element"""
        if start_node == None:
            start_node = self.root
        current_node = start_node
        if current_node == None:
            return None
        while(current_node.left_child != None):
            current_node = current_node.left_child
        return current_node

    def maximum(self, start_node = None) -> Node:
        """return the maximun element"""
        if start_node == None:
            start_node = self.root
        current_node = start_node
        if current_node == None:
            return None
        while(current_node.right_child != None):
            current_node = current_node.right_child
        return current_node

    def successor(self, current_node:Node) -> Node:
        """return the successor"""

        if current_node.right_child != None:
            return self.minimum(current_node.right_child)
        last_node = current_node
        current_node = current_node.parent
        while current_node!= None and last_node == current_node.right_child:
            last_node = current_node
            current_node = current_node.parent
        return current_node

    def successor_by_key(self,key) -> Node:
        """find the element and return the successor"""
        return self.successor(self.search(key))

    def predecessor(self, current_node:Node) -> Node:
        """return the predecessor"""
        if current_node.left_child != None:
            return self.maximum(current_node.left_child)
        last_node = current_node
        current_node = current_node.parent
        while current_node!= None and last_node == current_node.left_child:
            last_node = current_node
            current_node = current_node.parent
        return current_node

    def predecessor_by_key(self,key) -> Node:
        """find the element and return the predecessor"""
        return self.predecessor(self.search(key))

    def insert(self, key):
        """insert an element into the tree"""
        new_node = Node(key)
        current_node = self.root
        while 1:
            if key <= current_node.key:
                if current_node.left_child == None:
                    current_node.left_child = new_node
                    new_node.parent = current_node
                    return 0
                else:
                    current_node = current_node.left_child
            if key > current_node.key:
                if current_node.right_child == None:
                    current_node.right_child = new_node
                    new_node.parent = current_node
                    return 0
                else:
                    current_node = current_node.right_child

    def delete_by_key(self, key):
        """delete an element by key"""
        delete_node = self.search(key)
        if delete_node == None:
            return 0
        self.delete(delete_node)

    def delete(self, delete_node:Node):
        """delete an element"""
        if delete_node.left_child == None:
            if delete_node.right_child != None:
                delete_node.right_child.parent = delete_node.parent
            if delete_node.parent == None:
                self.root = delete_node.right_child
            else:
                if delete_node.parent.left_child == delete_node:
                    delete_node.parent.left_child = delete_node.right_child
                else:
                    delete_node.parent.right_child = delete_node.right_child
            del delete_node
            return 0
        if delete_node.right_child == None:
            if delete_node.left_child != None:
                delete_node.left_child.parent = delete_node.parent
            if delete_node.parent == None:
                self.root = delete_node.left_child
            else:
                if delete_node.parent.left_child == delete_node:
                    delete_node.parent.left_child = delete_node.left_child
                else:
                    delete_node.parent.right_child = delete_node.left_child
            del delete_node
            return 0
        if delete_node.right_child.left_child == None:
            delete_node.right_child.parent = delete_node.parent
            if delete_node.parent == None:
                self.root = delete_node.right_child
            else:
                if delete_node.parent.left_child == delete_node:
                    delete_node.parent.left_child = delete_node.right_child
                else:
                    delete_node.parent.right_child = delete_node.right_child
            delete_node.left_child.parent = delete_node.right_child
            delete_node.right_child.left_child = delete_node.left_child
            del delete_node
            return 0
        successor_node = self.minimum(delete_node.right_child)
        new_node = Node(successor_node.key)
        self.delete(successor_node)
        new_node.right_child = delete_node.right_child
        delete_node.right_child.parent = new_node
        delete_node.left_child.parent = new_node
        new_node.left_child = delete_node.left_child
        new_node.parent = delete_node.parent
        if delete_node.parent == None:
            self.root = new_node
        else:
            if delete_node.parent.left_child == delete_node:
                delete_node.parent.left_child = new_node
            else:
                delete_node.parent.right_child = new_node
        del delete_node
        return 0


a = [100,-20,10,0,1,-201,20,300,-329, 19, 21,22, 18,18.5,19]
tree = BinarySearchTree(a)
print(tree.successor_by_key(1).key)
tree.delete_by_key(100)
tree.inorder_tree_walk()
tree.preorder_tree_walk()
print(tree.successor_by_key(1).key)


