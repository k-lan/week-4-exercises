from pythonds.basic import Stack
from timeit import Timer
import time

"""
Solutions to exercises one and two.
Run main to view times and thrown exception
"""


def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    try:
        tokenList = infixexpr.split()
        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                        (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
    except:
        return f"Incorrect object type for infix expression.{TypeError}"

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    try:
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token, operand1, operand2)
                operandStack.push(result)
        return operandStack.pop()
    except:
        f"Incorrect object type for postfix expression.{TypeError}"


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def time_1():
    expr = "A * B + C * D"
    infixToPostfix(expr)


def time_2():
    expr = "A * B + C * D" * 1000
    infixToPostfix(expr)


def time_3():
    expr = infixToPostfix("A B * C D * +")
    start = time.time()
    postfixEval(expr)
    time.sleep(0.000001)
    end = time.time()
    print(f'Evaluate {end - start} seconds')


def time_4():
    expr = infixToPostfix("A B * C D * +" * 100)
    start = time.time()
    postfixEval(expr)
    time.sleep(0.000001)
    end = time.time()
    print(f'Evaluate {end - start} seconds')


def main():
    t1 = Timer("time_1()", "from __main__ import time_1")
    print("Convert ", t1.timeit(number=1000), "milliseconds")
    t2 = Timer("time_2()", "from __main__ import time_2")
    print("Convert ", t2.timeit(number=1000), "milliseconds")
    print(infixToPostfix(True))
    time_3()
    time_4()


if __name__ == '__main__':
    main()
