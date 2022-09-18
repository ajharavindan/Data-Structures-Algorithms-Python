from unittest import result


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

    """
    def min_value_node(self):
        temp = self.root
        while True:
            if temp.left is None:
                return temp.value
            temp = temp.left
        return None         """
    
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue)>0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def DFS_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
            
        
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.DFS_post_order())