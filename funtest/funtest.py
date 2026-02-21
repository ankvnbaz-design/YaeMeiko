import turtle

turtle.speed(3)
turtle.bgcolor("black")
turtle.pensize(3)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red", "pink")
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()

# Viết chữ ở giữa trái tim
turtle.penup()
turtle.goto(0, 80)  # Di chuyển đến vị trí giữa trái tim
turtle.color("blue")
turtle.write("Love You", align="center", font=("Arial", 20, "bold"))

turtle.hideturtle()
turtle.done()
