"""
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-2^(31) <= val <= 2^(31) - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

# To solve the problem, we need two stacks. One stack to keep track of all the elements and another stack to keep track of the minimum elements.
class MinStack(object):

    def __init__(self):
        # First, we declare the variables, and since we are dealing with stacks, we use an empty list.
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        Next, we define the push function.
        A push function should push a value into the stack and if the stack is empty or the value is less than or equal to the current minimum, it will be appended to the stack.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):
        """
        Next, we define the pop function.
        The pop function should remove the top element in the stack. 
        If the element is equal to the current minimum, it will be removed from the stack.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        # Next, we define the top function. This just returns the top element of the stack.
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        # Next, we define the get minimum function. This returns the top element of the stack which is the minimum element in the stack.
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()