class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                if (b*a<0):
                    if b%a != 0:
                        stack.append((b//a)+1)
                    else:
                        stack.append((b//a))

                else:
                    stack.append(b//a)
            else:
                stack.append(int(t))
        return stack[0]