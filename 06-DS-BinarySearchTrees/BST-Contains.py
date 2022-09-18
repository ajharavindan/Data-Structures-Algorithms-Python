class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)      #Create a new node

        if self.root is None:       #if the tree is empty or root is none 
            self.root = new_node    #then insert the new node at root
            return True             #return true to come out of the method

        temp = self.root            #create temp that is pointing to the root

        while True:                 #While loop to reach to the point of insertion 

            if new_node == temp:    #If the new node and the node pointing at temp are same
                return False        #return false to come out of the method (Since the nodes should be unique in a tree)

            if new_node.value < temp.value:     #If the value of new node is less than the value of node in which temp is pointing

                if temp.left is None:           #If the node in which temp is pointing doesn't have left sub node
                    temp.left = new_node        # New node is inserted as a sub left node of the node in which temp is pointing
                    return True                 #return true to come out of the method

                temp = temp.left                #If the node in which temp is pointing have left sub node then make the temp variable point to the left sub node      

            else:                               #If the value of new node is greater than the value of node in which temp is pointing

                if temp.right is None:          #If the node in which temp is pointing doesn't have right sub node
                    temp.right = new_node       # New node is inserted as a sub right node of the node in which temp is pointing
                    return True                 #return true to come out of the method

                temp = temp.right               #If the node in which temp is pointing have right sub node then make the temp variable point to the right sub node
    
    """
    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root
        while True:
            if temp.value == value:
                return True
            else:
                if value < temp.value:
                    if temp.left is None:
                        return False
                    temp = temp.left
                
                else:
                    if temp.right is None:
                        return False
                    temp = temp.right       """

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(100)
my_tree.insert(99)
my_tree.insert(101)
my_tree.insert(102)

print(my_tree.contains(99))
print(my_tree.contains(98))
