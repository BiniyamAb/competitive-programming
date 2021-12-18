from typing import List
import math

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        if tokens[i] in "*/-+":
            if len(stack) > 1: 
                if tokens[i] == "*":
                    res = int(stack.pop()) * int(stack.pop())
                    stack.append(res)
                elif tokens[i] == "+":
                    res = int(stack.pop()) + int(stack.pop())
                    stack.append(res)
                elif tokens[i] == "/":
                    num = int(stack.pop())
                    res = int(stack.pop()) / num
                    if res < 0: res = int(math.ceil(res)) 
                    else: res = int(math.floor(res))
                    stack.append(res)
                elif tokens[i] == "-":
                    num = int(stack.pop())
                    res = int(stack.pop()) - num 
                    stack.append(res)
        else:
            stack.append(int(tokens[i]))

    return int(stack[0])