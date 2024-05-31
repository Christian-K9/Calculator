import tkinter as tk

equation = ""

#button click functions
def number_click(number):
    global equation
    global ending_index
    num = str(number)
    equation = equation + num
    label.config(text = equation, bg = "gray", font = ("Arieal", 10))

def operator_click(operator):
    global equation
    global starting_index
    global ending_index
    if (operator == "^"):
        operator = "**"
    equation = equation + operator
    label.config(text = equation, bg = "gray", font = ("Arieal", 10))

def clear_click():
    global equation
    equation = ""
    label.config(text = equation, bg = "gray")
    
def remove_click():
    global equation
    equation_length = len(equation)
    equation = equation[0:equation_length - 1]
    label.config(text = equation, bg = "gray")
        
def equal_click():
    try:
        result = eval(equation)
        answer.config(text = result)
        answer.place(x = 0, y = 50)
    except Exception as e:
        print(f"Error: {e}")
        
        
#main application window
root = tk.Tk()
root.geometry("400x300")

#number buttons
y_cordinate = 150
number = 1
for i in range(3):
    for j in range(3):
        x_cordinate = j * 50
        i = tk.Button(root, text = number, command= lambda num=number: number_click(num))
        i.place(x = x_cordinate, y = y_cordinate)
        number = number + 1
    y_cordinate = y_cordinate + 50


#operators
add = tk.Button(root, text = "+", command = lambda: operator_click("+"))
subtract = tk.Button(root, text = "-", command = lambda: operator_click("-"))
multiply = tk.Button(root, text = "*", command = lambda: operator_click("*"))
divide = tk.Button(root, text = "/", command = lambda: operator_click("/"))
exponent = tk.Button(root, text = "^", command = lambda: operator_click("^"))
openingParenthesis = tk.Button(root, text = "(", command = lambda: operator_click("("))
closingParenthesis = tk.Button(root, text = ")", command = lambda: operator_click(")"))
decimal = tk.Button(root, text = ".", command = lambda: operator_click("."))

add.place(x = 200, y = 150)
subtract.place(x = 250, y = 150)
multiply.place(x = 300, y = 150)
divide.place(x = 350, y = 150)
exponent.place(x = 200, y = 200)
openingParenthesis.place(x = 250, y = 200)
closingParenthesis.place(x = 300, y = 200)
decimal.place(x = 350, y = 200)

#label
label = tk.Label(root, text = equation, bg = "gray", font = ("Arieal", 10))
label.place(x = 0, y = 0)

answer = tk.Label(root, text = "Answer", bg = "green", font = ("Arieal", 20))
answer.place(x = 0, y = 50)

#clear sign
clear = tk.Button(root, text = "Clear", command = clear_click)
clear.place(x = 200, y = 250)

#remove sign
remove = tk.Button(root, text = "<", command = remove_click)
remove.place(x = 300, y = 250)

#equal sign
equal = tk.Button(root, text = "=", command = equal_click)
equal.place(x = 350, y = 250)


root.mainloop()
