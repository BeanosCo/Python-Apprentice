"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

from tkinter import messagebox, simpledialog, Tk

# Create a window object

window = Tk()

# Hide the window, hint: use the withdraw method

window.withdraw()

# Ask the user for the first number  

num1 = simpledialog.askfloat("Your Calc", "What is the first number?")

# Ask the user for the second number

num2 = simpledialog.askfloat("Your Calc", "What is the second number?")

# Ask for an Operator

operator = simpledialog.askstring("Your Calc", "Input an operator in words")

# Display the sum of the two numbers

if operator == "add":
    product = num1 + num2

elif operator == "multiply":
    product = num1 * num2

elif operator == "divide":
    product = num1 / num2

elif operator == "subtract":
    product = num1 - num2

messagebox.showinfo('Your Addition', product)

# Keep the window open

window.mainloop()