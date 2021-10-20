class Node:                         
    def __init__(self, value):              
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None            

    def insert(self, value):        
        new_node = Node(value)      
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

    def BFS(self):          #Breadth First Search
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_PreOrder(self):         #Deapth First Search -> Pre Order
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def DFS_PostOrder(self):        #Deapth First Search -> Post Order
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def DFS_InOrder(self):          #Deapth First Search -> In Order
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results 


my_tree = BST()
my_tree.insert(47)
my_tree.insert(11)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)