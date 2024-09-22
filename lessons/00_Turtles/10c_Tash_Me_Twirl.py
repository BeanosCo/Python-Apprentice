
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

import turtle 
turtle.setup(width=600, height=600) 

turtle.penup()

turtle.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

#set_turtle_image(turtle, "moustache1.gif")

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

screen = turtle.Screen()
set_background_image(screen, "emoji.png")

def turtle_clicked(turtle, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        turtle.tilt(20) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
turtle.onclick(lambda x, y, turtle=turtle: turtle_clicked(turtle, x, y))

turtle.done()