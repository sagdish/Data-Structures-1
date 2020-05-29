"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../myQueue')
sys.path.append('../stack')
# print(sys.path)
from stack import Stack
from myQueue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
        else:
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)

        print(node.value)
        
        if self.right:
            self.right.in_order_print(self.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # print('hereis node: ', node)       
        newQueue = Queue()
        newQueue.enqueue(node)

        while newQueue:
            node = newQueue.dequeue()
            print(node.value)
            if node.left:
                newQueue.enqueue(node.left)
            if node.right:
                newQueue.enqueue(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        myStack = Stack()
        myStack.push(node)

        while myStack:
            node = myStack.pop()
            if node.right:
                myStack.push(node.right)
            if node.left:
                myStack.push(node.left)
            print(node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# test of imports:
# newQueue = Queue()
# newQueue.enqueue(BSTNode(3))
# print(newQueue.dequeue().left)