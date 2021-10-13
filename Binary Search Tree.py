class BST:
    def __init__(self):
        self.root = None            # the BST initialization can also be done in following way:-
                                    # def __init__(self, value):
    def insert(self, value):        # new_node = Node(value)
        new_node = Node(value)      # self.root = new_node
        temp = self.root
        if self.root is None:
           self.root = new_node
           return True
        else:
            while temp:             # while (True)
                if new_node.value == temp.value:
                    return False
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

class Node:                         
    def __init__(self, value):              
        self.value = value
        self.left = None
        self.right = None

my_tree = BST()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(8)
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(0)

print(my_tree.contains(2))
print(my_tree.contains(6))
print(my_tree.contains(5))
print(my_tree.contains(11))         