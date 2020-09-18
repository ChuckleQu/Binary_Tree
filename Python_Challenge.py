import random
from Binary_tree_functions import BinaryTree, create_tree, print_tree

list_of_numbers = []
for n in range(0, 100):                      # Create 100 random numbers and store it in "list_of_numbers".
    number = random.randint(0, 100)
    list_of_numbers.append(number)

my_tree = BinaryTree(list_of_numbers)        # Initialize "list_of_numbers": equip it with "LeftChild" and "RightChild".
my_tree = create_tree(my_tree)               # Call function "create_tree" to create the tree.

print('node\t\tmin\t\tmax\t\tnum_of_points')   # Print the title.
print_tree(my_tree)                          # Call function "print_tree" to print out the required information.

# Note that when print out "my_tree", I place a blank line when one level is end.
# This can help us to identify different levels.
# If you don't like this blank line, you can also delete it by deleting the line 58 in "Binary_tree_function.py" file.
