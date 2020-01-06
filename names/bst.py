class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        # keep going (recursion)
        # if greater than or equal to then go right, make a new tree/node if empty, otherwise
        # keep going.

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value, return it
        # go left or right based on smaller or bigger
        if target != self.value:
            if target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            elif target >= self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
        else:
            return self.value

    # Return the maximum value found in the tree

    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right:
            self.value = self.right.get_max()
        return self.value
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
    # DAY 2 Project -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # Recurse through self.left values until reaching the end
        if self.left:
            self.left.in_order_print(self.left)
        # Print all left values
        print(self.value)
        # Print all right values
        if self.right:
            self.right.in_order_print(self.right)

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            removed = queue.dequeue()
            print(removed.value)
            if removed.left:
                queue.enqueue(removed.left)
            if removed.right:
                queue.enqueue(removed.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        # Create a new stack
        stack = Stack()
        # Put root in the stack
        stack.push(node)

        while stack.size > 0:
            removed = stack.pop()
            print(removed.value)
            if removed.left:
                stack.push(removed.left)
            if removed.right:
                stack.push(removed.right)
