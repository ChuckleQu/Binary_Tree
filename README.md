# Binary-Tree
## Python Challenge 2020/09/18
I have two files to built my binary tree. One is the file used to store class and functions, *Binary_Tree_Fuctions.py*. Another is the file used to execute, *Python_Changes.py*. Let's see *Binary_Tree_Fuctions.py* first.

## Binary_Tree_functions.py
As I mentioned above, this file is used to store class and functions. There are one class (iniside of the class, there are five functions) and three functions (outside of the class) in the file.

1. fuction creat_numbers
```python
def create_numbers():
    list_of_numbers = []
    while len(list_of_numbers) < 100:
        number = random.randint(0, 100)
        if list_of_numbers.count(number) <= 4:
            list_of_numbers.append(number)
    return list_of_numbers
```
This function is used to create a number list whose identical numbers are not greater than 5. Note that if the identical numbers are more than 5. It will cause error. Later, we will talk about this possible error in detail.

2. class BinaryTree
```python
class BinaryTree:
    def __init__(self, rootObj, name=None):       # Initialize the data by creating its "LeftChild", "RightChild" and name.
        self.root = rootObj
        self.name = name
        self.leftChild = None
        self.rightChild = None

    def add_level(self):                          # This function is used to add level at the needed nodes.
        length = max(self.root) - min(self.root)  # the following 4 lines shows how I separate the exiting list into two parts.
        half_length = length / 2
        left = [num for num in self.root if num <= min(self.root) + half_length]
        right = [num for num in self.root if num > max(self.root) - half_length]
        self.leftChild = BinaryTree(left, self.name + 'L')       # For the "leftChild", the name will plus "L"
        self.rightChild = BinaryTree(right, self.name + 'R')     # For the "rightChild", the name will plus "R"

    def getRightChild(self):                         # We can call this function to return the "rightChild" value.
        return self.rightChild                       

    def getLeftChild(self):                          # We can call this function to return the "leftChild" value.
        return self.leftChild

    def getRootValue(self):                          # We can call this function to return the "root" value.
        return self.root
```

3. function create_tree
```python
def create_tree(tree):                     # The function "create_tree" is used to create our tree.
    if len(tree.getRootValue()) > 5:       # Specify the terminating condition (not greater than 5 points).
        tree.add_level()
        create_tree(tree.getLeftChild())   # We use pre-order to check the nodes who satisfy the condition "length > 5",
        create_tree(tree.getRightChild())  # and create a new level at these satisfying nodes.
    return tree
```

4. function print_tree
```python
def print_tree(root):        # This function is used to print our nodes from "top to bottom" and "left to right".
    queue = [root]           # "queue" is a list containing the roots in the current level.
    toBePrintedNodes = 1     # Represent the number of nodes in the current level that have not yet been printed.
    nextLevelNodes = 0       # Represent the number of nodes at next level.

    while len(queue) > 0:
        currentRoot = queue.pop(0)     # Delete the first root in the current "queue" and store its value in "currentRoot".
        print(f'{currentRoot.name}\t\t{min(currentRoot.root)}\t\t{max(currentRoot.root)}\t\t{len(currentRoot.root)}')
        # Print this node's name, minimum value, maximum value and length

        if currentRoot.leftChild:                  # If this root has a "leftChild", then we will:
            queue.append(currentRoot.leftChild)    # 1. Add its "leftChild" to "queue".
            nextLevelNodes += 1                    # 2. The number of nodes at next level will plus 1.

        if currentRoot.rightChild:                 # Same as "rightChild"
            queue.append(currentRoot.rightChild)
            nextLevelNodes += 1

        toBePrintedNodes -= 1                  # Number of nodes that should be printed in the current level will minus 1.


        if toBePrintedNodes == 0:
        # If there is nothing at the next level, the program is no longer executed
            if nextLevelNodes == 0:
                break
            print()                            # I place a blank line here to identify the current level is end.
            toBePrintedNodes = nextLevelNodes  # The number of "toBePrintedNodes" in the new cycle is "nextLevelNodes".
            nextLevelNodes = 0                 # We reset the "nextLevelNodes". Let it count the number in the new cycle.
```

All the class and functions used to build the tree have been introduced. Now, let's see the the file used to execute.

## 2. Python_Changes.py
In this file, I call the functions from *Binary_Tree_Fuctions.py* to help us build the tree.

1. import the class and functions from *Binary_Tree_Fuctions.py*.
```python
from Binary_Tree_Functions import BinaryTree, create_tree, print_tree, create_numbers
```

2. We call the function *create_numbers* to help us creat the numbers.
```python
list_of_numbers = create_numbers()           # Create 100 random numbers and store it in "list_of_numbers".
```
This function will create a list of numbers whose identical numbers are not greater than 5. Note that if the identical numbers are more than 5. It will cause error. Let's see what will happen if the identical numbers are more than 5.
 
![Image of Error](https://img.overpic.net/images/w/4/7/xw47mznc5nhqm7hyh7ey6.png)

Why there will be an error? To figure out why, let's add one line in the add_level function.
```python
    def add_level(self):
        length = max(self.root) - min(self.root)
        half_length = length / 2
        left = [num for num in self.root if num <= min(self.root) + half_length]
        right = [num for num in self.root if num > max(self.root) - half_length]
        print('Add level', left, right)                                         # We add a 'print' here!
        self.leftChild = BinaryTree(left, self.name + 'L')
        self.rightChild = BinaryTree(right, self.name + 'R')
```
Now, run the code several time untill the error comes out again and see what are printed on the terminal.

![Image of Error_Output](https://img.overpic.net/images/8/n/r/x8nr6ibfbjslf75kjj5bf.png)

For the 6 identical number "96", the add_level function can not seperate them into smaller parts. However, since the length of the list is greater than 5, the function will try to seperate them again and again and finally cause the error. To avoid this kind of circumstances, when produce numbers, we can't let it create more than five identical numbers.

3. Initialize "list_of_numbers": equip it with "LeftChild", "RightChild", name it "X" and store the result in *my_tree*.
```
my_tree = BinaryTree(list_of_numbers, 'X')
```

4. Call function "create_tree" to create the tree and store the result in *my_tree*.
```
my_tree = create_tree(my_tree)
```

5. Call function "print_tree" to print out the required information.
```
print('node\tmin\t\tmax\t\tnum_of_points')     # Print the title.
print_tree(my_tree)                            # Print the tree.
```

## Output Example
```
node		min		max		num_of_points
X		0		100		100

XL		0		48		54
XR		51		100		46

XLL		0		24		28
XLR		25		48		26
XRL		51		72		21
XRR		76		100		25

XLLL		0		12		15
XLLR		14		24		13
XLRL		25		35		15
XLRR		37		48		11
XRLL		51		61		12
XRLR		62		72		9
XRRL		76		88		11
XRRR		89		100		14

XLLLL		0		6		11
XLLLR		7		12		4
XLLRL		14		19		8
XLLRR		20		24		5
XLRLL		25		30		8
XLRLR		32		35		7
XLRRL		37		42		8
XLRRR		43		48		3
XRLLL		51		56		7
XRLLR		58		61		5
XRLRL		62		66		4
XRLRR		68		72		5
XRRLL		76		81		6
XRRLR		83		88		5
XRRRL		89		94		5
XRRRR		95		100		9

XLLLLL		0		3		5
XLLLLR		4		6		6
XLLRLL		14		16		4
XLLRLR		17		19		4
XLRLLL		25		26		4
XLRLLR		28		30		4
XLRLRL		32		32		3
XLRLRR		34		35		4
XLRRLL		37		39		7
XLRRLR		42		42		1
XRLLLL		51		53		3
XRLLLR		54		56		4
XRRLLL		76		76		2
XRRLLR		79		81		4
XRRRRL		95		97		4
XRRRRR		98		100		5

XLLLLRL		4		4		4
XLLLLRR		6		6		2
XLRRLLL		37		38		5
XLRRLLR		39		39		2
```
Note that when print out "my_tree", I place a blank line when one level is end. This can help us to identify different levels. If you don't like this blank line, you can also delete it by deleting the *print()* at line 70 in "Binary_tree_function.py" file.

To get the output text file, we can type "python<file_name.py>output_file_name.txt" into terminal.
