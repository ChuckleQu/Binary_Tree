class BinaryTree:
    def __init__(self, rootObj, name='X'):           # Initialize the data by creating its "LeftChild" and "RightChild".
        self.root = rootObj
        self.name = name
        self.leftChild = None
        self.rightChild = None

    def add_level(self):                             # This function is used to add level at the needed nodes.
        length = max(self.root) - min(self.root)     # line 8-11 shows how I separate the exiting list into two parts.
        half_length = length / 2
        left = [num for num in self.root if num <= min(self.root) + half_length]
        right = [num for num in self.root if num > max(self.root) - half_length]
        self.leftChild = BinaryTree(left, self.name + 'L')      # Call "BinaryTree" to initialize the new created nodes.
        self.rightChild = BinaryTree(right, self.name + 'R')

    def getRightChild(self):                         # We can call this function to return the "rightChild".
        return self.rightChild

    def getLeftChild(self):                          # We can call this function to return the "leftChild".
        return self.leftChild

    def getRootValue(self):                          # We can call this function to return the "root".
        return self.root


def create_tree(tree):                     # The function "create_tree" is used to create our tree.
    if len(tree.getRootValue()) > 5:       # Specify the terminating condition (not greater than 5 points).
        tree.add_level()                   # (Well, it is equivalent to say "if length > 5, execute the code".)
        create_tree(tree.getLeftChild())
        create_tree(tree.getRightChild())  # We use pre-order to check the node who satisfy the condition "length > 5",
    return tree                            # and create a new level at these satisfying nodes.


def print_tree(root):        # This function is used to print our nodes from "top to bottom" and "left to right".
    queue = [root]           # "queue" is a list containing the roots in the current level.
    toBePrintedNodes = 1     # Represent the number of nodes in the current level that have not yet been printed.
    nextLevelNodes = 0       # Represent the number of nodes at next level.

    while len(queue) > 0:
        currentRoot = queue.pop(0)     # Delete the first root and store its value in "currentRoot".
        print(f'{currentRoot.name}\t\t{min(currentRoot.root)}\t\t{max(currentRoot.root)}\t\t{len(currentRoot.root)}')

        if currentRoot.leftChild:                  # If this root has a "leftChild", then we will:
            queue.append(currentRoot.leftChild)    # 1. Add its "leftChild" to "queue".
            nextLevelNodes += 1                    # 2. The number of nodes at next level will plus 1.

        if currentRoot.rightChild:                 # Same for "rightChild"
            queue.append(currentRoot.rightChild)
            nextLevelNodes += 1

        toBePrintedNodes -= 1                      # The nodes that should be printed in the current level will minus 1.

        # If the number of unprinted nodes in the current level is 0, it jumps to the next level
        if toBePrintedNodes == 0:
            # If there is nothing at the next level, the program is no longer executed
            if nextLevelNodes == 0:
                break                            # I place a blank line here to identify the current level is end.
            print()                              # The next line is the next level.
            toBePrintedNodes = nextLevelNodes    # The number of "toBePrintedNodes" in the new cycle is "nextLevelNodes"
            nextLevelNodes = 0               # We reset the "nextLevelNodes". Let it collect the number in the new cycle

# Execute python<yourPythonFile.py>outputfile.txt at Terminal to get txt file of the output.
