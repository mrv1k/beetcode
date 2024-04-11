class Solution:
  def evalRPN(self, tokens):
    stack = []
    symbols = ['+', '-', '*', '/']
    for char in tokens:
        if char in symbols:
            b = int(stack.pop())
            a = int(stack.pop())
            if char == '+':
                stack.append(a + b)
            if char == '-':
                stack.append(a - b)
            if char == '*':
                stack.append(a * b)
            if char == '/':
                stack.append(int(a / b))
        else:    
            stack.append(char)
    return int(stack[0])

x = Solution()
# x.evalRPN(["2","1","+","3","*"])
x.evalRPN(["1","2","+"])
x.evalRPN(["1","2","-"])
x.evalRPN(["1","2","*"])
x.evalRPN(["2","2","/"])

x.evalRPN(["5","2","/"])
x.evalRPN(["5","-2","/"])

y = ["4","13","5","/","+"]
x.evalRPN(y)
