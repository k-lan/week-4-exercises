import turtle
import random
"""
Run main to view tree, was able to get the leaves, branch thickness, and colors set up.
"""


def tree(branchLen, branchWid, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        if branchWid > 0:
            t.pensize(branchWid - 1)
        if branchLen < 31:
            t.color("green")
        tree(branchLen - random.randint(10, 20), branchWid - 2, t)
        t.pensize(1)
        t.left(40)
        if branchWid > 0:
            t.pensize(branchWid - 1)
        if branchLen < 40:
            t.color("green")
        tree(branchLen - random.randint(10, 20), branchWid - 2, t)
        t.pensize(1)
        t.right(20)
        t.backward(branchLen)
        t.color("brown")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.pensize(10)
    tree(75, 10, t)
    myWin.exitonclick()


main()
