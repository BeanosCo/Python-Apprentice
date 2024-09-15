
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)  

square = 4
pentagon = 5
hexagon = 6

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(50)                              # Move tina forward by the forward distance
        tina.left(angle)                            # Turn tina left by the left turn


draw_polygon(square)                        # Draw a square

tina.penup()
tina.goto(100,0)
tina.pendown()                                      # Move tina to another spot on the screen

draw_polygon(pentagon)                        # Draw a pentagon

tina.penup()
tina.goto(-100,0)
tina.pendown()                                     # Move tina to another spot on the screen

draw_polygon(hexagon)                        # Draw a hexagon


turtle.exitonclick()                     # Close the window when we click on it
