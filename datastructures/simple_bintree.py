"""Simple implementation of a binary tree."""

class Node(object):
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d
    def get_left(self):
        return self.left
    def set_left(self, n):
        self.left = n
    def get_right(self):
        return self.right
    def set_right(self, n):
        self.right = n
    def get_data(self):
        return self.data
    def set_data(self, n):
        self.data = n
    """Removes the required node from the binary tree. Returns True upon successful completion, False otherwise."""
    def remove(self, d, parent):
        if(d < self.get_data()):
            if(self.get_left() != None):
                return self.get_left().remove(d, self)
            else:
                return False
        elif(d > self.get_data()):
            if(self.get_right() != None):
                return self.get_right().remove(d, self)
            else:
                return False
        else:
            if(self.get_left() != None and self.get_right() != None):
                self.set_data(self.get_right().min())
                self.get_right().remove(self.get_data(), self)
            elif(parent.get_left() == self):
                if(self.get_left() != None):
                    parent.set_left(self.get_left())
                else:
                    parent.set_left(self.get_right())
            elif(parent.get_right() == self):
                if(self.get_left() != None):
                    parent.set_right(self.get_left())
                else:
                    parent.set_right(self.get_right())
            return True
    """Returns the minimum value in a given subtree."""
    def min(self):
        if(self.get_left() == None):
            return self.get_data()
        else:
            return self.get_left().min()
        
"""Class used to create a binary tree."""
class BinaryTree(object):
    def __init__(self):
        self.root = None
    """Checks whether the binary tree is empty."""
    def is_empty(self):
        if(self.root == None):
            return True
        return False
    def add(self, d):
        if(self.root == None):
            self.root = Node(d)
        else:
            self._add(d, self.root)
    """Adds a new node to the tree."""
    def _add(self, d, n):
        if(n != None):
            if(d < n.get_data()):
                self._add(d, n.get_left())
                if(n.get_left() == None):
                    n.set_left(Node(d))
            else:
                self._add(d, n.get_right())
                if(n.get_right() == None):
                    n.set_right(Node(d))
    def print_tree(self):
        if(self.is_empty() == False):
            self._print_tree(self.root)
    """Traverses the tree, printing each value in inorder traversal."""
    def _print_tree(self, n):
        if(n != None):
            self._print_tree(n.get_left())
            print(str(n.get_data()) + ' ')
            self._print_tree(n.get_right())
    def find(self, d):
        if(self.is_empty() == False):
            self._find(d, self.root)
    """Assuming the tree is not empty, searches the tree for a specified value and returns it if found."""
    def _find(self, d, n):
        if(n != None):
            if(d == n.get_data()):
                print(str(d) + " found")
            elif(d < n.get_data()):
                return self._find(d, n.get_left())
            else:
                return self._find(d, n.get_right())
    """Checks for the special case where the node to be removed is the root node and makes appropriate calls to the remove function in the Node class. Returns True if the node was deleted, False otherwise."""
    def remove(self, d):
        if(self.is_empty()):
            return False
        else:
            if(self.root.get_data() == d):
                temp_root = Node(0)
                temp_root.set_left(self.root)
                result = self.root.remove(d, temp_root)
                self.root = temp_root.get_left()
                return result
            else:
                return self.root.remove(d, None)
    def distance(self, d1, d2):
        if(self.is_empty() == False):
            return self._distance(d1, d2, self.root)
        return None
    def _distance(self, d1, d2, n):
        if(d1 == d2):
            return 0
        else:
            if(d1 > n.get_data() and d2 > n.get_data()):
                return self._distance(d1, d2, n.get_right())
            elif(d1 < n.get_data() and d2 < n.get_data()):
                return self._distance(d1, d2, n.get_left())
            elif(d1 == n.get_data()):
                return self.get_distance(d2, n, 0)
            elif(d2 == n.get_data()):
                return self.get_distance(d1, n, 0)
            else:
                return self.get_distance(d1, n, 0) + self.get_distance(d2, n, 0)
    def get_distance(self, d, n, dist):
        if(d == n.get_data()):
            return dist
        elif(d < n.get_data()):
            return self.get_distance(d, n.get_left(), dist+1)
        else:
            return self.get_distance(d, n.get_right(), dist+1)
"""demo"""
b = BinaryTree()
print("Adding 10, 6, 11, 22, 1, and 7 to the binary tree in that order:")
b.add(10)
b.add(6)
b.add(11)
b.add(22)
b.add(1)
b.add(7)
print("Nodes in the tree(in-order traversal):")
b.print_tree()
print("Distance from 1 to 22: " + str(b.distance(1, 22)))
print("Is 7 in the tree?")
b.find(7)
print("Removes 10 from the tree:")
print(b.remove(10))
print("Nodes in the tree(in-order traversal):")
b.print_tree()
