import turtle;

tree = turtle.Turtle()
tree.left(90)
tree.speed(10)

tree.goto(0,-20)

tree.color("#fff")
turtle.Screen().bgcolor("#000")

def draw(i):
    if (i<10):
        return
    else:
        tree.forward(i)
        tree.left(30)
        draw(3*i/4)
        tree.right(60)
        draw(3*i/4)
        tree.left(30)
        tree.backward(i)

draw(120)