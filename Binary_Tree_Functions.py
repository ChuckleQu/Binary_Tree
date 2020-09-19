import random
import sys


class Logger(object):                             # This class is used to keep output into a txt file.
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


# Create a number list whose identical numbers are not greater than 5.
def create_numbers():                          # Note the if the identical numbers are more than 5. It will cause error.
    list_of_numbers = []
    while len(list_of_numbers) < 100:
        number = random.randint(0, 100)
        if list_of_numbers.count(number) <= 4:
            list_of_numbers.append(number)
    return list_of_numbers


class BinaryTree:
    def __init__(self, rootObj, name=None):    # Make change here: add "name" to __init__.
        self.root = rootObj
        self.name = name
        self.leftChild = None
        self.rightChild = None

    def add_level(self):
        length = max(self.root) - min(self.root)
        half_length = length / 2
        left = [num for num in self.root if num <= min(self.root) + half_length]
        right = [num for num in self.root if num > max(self.root) - half_length]
        self.leftChild = BinaryTree(left, self.name + 'L')       # For the "leftChild", the name will plus "L"
        self.rightChild = BinaryTree(right, self.name + 'R')     # For the "rightChild", the name will plus "R"

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootValue(self):
        return self.root


def create_tree(tree):
    if len(tree.getRootValue()) > 5:
        tree.add_level()
        create_tree(tree.getLeftChild())
        create_tree(tree.getRightChild())
    return tree


def print_tree(root):
    queue = [root]
    toBePrintedNodes = 1
    nextLevelNodes = 0

    while len(queue) > 0:
        currentRoot = queue.pop(0)
        print(f'{currentRoot.name}\t\t{min(currentRoot.root)}\t\t{max(currentRoot.root)}\t\t{len(currentRoot.root)}')
        # Make change here: we print "currentRoot.name" instead of "nodeNumber"

        if currentRoot.leftChild:
            queue.append(currentRoot.leftChild)
            nextLevelNodes += 1

        if currentRoot.rightChild:
            queue.append(currentRoot.rightChild)
            nextLevelNodes += 1

        toBePrintedNodes -= 1

        if toBePrintedNodes == 0:
            if nextLevelNodes == 0:
                break
            print()
            toBePrintedNodes = nextLevelNodes
            nextLevelNodes = 0
