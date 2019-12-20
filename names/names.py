import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# RUNTIME: O(n^2)

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Create BST and append first value
NamesBST = BinarySearchTree(names_1[0])

# For the rest of values in names_1, insert into BST
for i in range(1, len(names_1)):
    NamesBST.insert(names_1[i])

# Compare names in names_2 using contains method and append to duplicates if a match
duplicates = []
for i in range(0, len(names_2)):
    if NamesBST.contains(names_2[i]):
        duplicates.append(names_2[i])


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
