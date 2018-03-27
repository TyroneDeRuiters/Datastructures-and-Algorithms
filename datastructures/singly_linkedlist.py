# singly-linked list implementation in python

class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
class LinkedList(object):
    def __init__(self):
        self.root = None
        self.size = 0
    def get_size():
        return self.size
    """A new node is added to the front of the list."""
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    """ removes the fist occurrence of a node with a given value, returning True if it exists. If not, False is retured."""
    def remove (self, d):
        this_node = self.root
        prev_node = None
        while(this_node):
            if(this_node.get_data() == d):
                if(prev_node):
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # data was successfully removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False #did not find dat
    """ Finds a node in the list and returns the value of the node if found, or None if not found."""
    def find(self, d):
        this_node = self.root
        while(this_node):
            if(this_node.get_data() == d):
                return d
            else:
                this_node = this_node.get_next()
        return None
    """Displays all nodes in the list."""
    def printList(self):
        this_node = self.root
        output = ""
        while(this_node):
            output += this_node.get_data() + " "
            this_node = this_node.get_next()
        print(output)
        
"""demo"""  
my_list = LinkedList()
my_list.add("A")
my_list.add("B")
my_list.add("C")
my_list.printList()
my_list.remove("B")
my_list.printList()
print(my_list.find("A"))
