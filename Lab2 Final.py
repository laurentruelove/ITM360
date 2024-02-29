# Lab2: Develop a Simple Calculator GUI with Tkinter
# Due: Feb 28 @ 11:59pm.
# Referring to your own OS, develop a calculator GUI to achieve the following goals:

"""
1. Following your expectation about this app, create respective widgets to allow user inputs,
 and further implement effective geometry management methods to manage the layout.

2. GUI Interface
In general, your GUI's interface is expected to be consistent with the calculator App installed in your own OS. 

Taking Mac Calculator as an example:
- the widgets for all the symbols, including result, operands, as well as operators, are placed and spanned 
in alignment with your desktop app. E.g., result at the top, '0', '.', and '=' are at the bottom.
- the widegets are expected to have different background colors. E.g., numbering operands are in light grey but 
regular operators are in orange.
- In general, all the widgets are placed in a structured, table-like layout.

3. GUI Functions
While your desktop calculator can do many calculations, like conversions and scentific calculations, for the sake of 
simplicity, this Lab expects the following basic arithmetic functions. 

Taking Mac Calculator as an example, we need to define several functions to determine any calculation:
- When an user clicks a number, the number will show up in the result widget and be added into any previous expression;
- When an user clicks the floating point operator, '.', the operator will be added into the expression and the updated value will show up
in the result widget;
- When an user clicks any regular operator, add('+'), subtract('-'), division('\u00F7') and multiplication('X'), the operator will NOT show up 
in the result widget but will be added into an expression;
- When an user clicks the clear symbol ('C'), any previous inputs will be cleared;
- When an user clicks the negation symbol ('+/-'), any input from previous step will be substracted from 0;
- When an user clicks the percentage symbol ('%'), any input from previous step will be divided by 100;
- When an user clicks the equal symbol ('='), the expression with any previous inputs will be calculated and the expression will be cleared.
If there is a zero division, an error should be displayed.

- Parse the functions into respective widgets.

"""

import tkinter as tk
from functools import partial
from tkmacosx import Button

class MacCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Mac Calculator")

        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.display = tk.Label(master, textvariable=self.display_var, bg="gray55", fg="white", font=("Helvetica", 36), anchor="e", padx=20)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons
        buttons = [
            ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),  
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col, *colspan) in buttons:
            if text in ['/', '*', '-', '+']:  # Check if the button is an operator
                btn = tk.Button(master, text=text, font=("Helvetica", 24), bg='dark orange', fg="white", bd=0, padx=20, pady=20, command=partial(self.on_operator_click, text))
            else:
                btn = tk.Button(master, text=text, font=("Helvetica", 24), bg='gray55', fg="white", bd=0, padx=20, pady=20, command=partial(self.on_button_click, text))
            btn.grid(row=row, column=col, columnspan=sum(colspan) if colspan else 1, sticky="nsew")
            master.grid_columnconfigure(col, weight=1)
            master.grid_rowconfigure(row, weight=1)

        master.grid_columnconfigure(0, weight=1)

        self.expression = ""

    def on_button_click(self, text):
        if text == 'AC':
            self.expression = ""
            self.display_var.set('0')
        elif text == '+/-':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.display_var.set(self.expression)
        elif text == '%':
            if self.expression:
                self.expression = str(float(self.expression) / 100)
                self.display_var.set(self.expression)
        elif text == '=':
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except ZeroDivisionError:
                self.display_var.set("Error")
                self.expression = ""
            except Exception as e:
                self.display_var.set("Error")
                self.expression = ""
        elif text.isdigit() or text == '.':
            if self.expression == '0':
                self.expression = text
            else:
                self.expression += text
            self.display_var.set(self.expression)

    def on_operator_click(self, text):
        # Check if the expression ends with a number
        if self.expression and self.expression[-1].isdigit():
            # Check if the operator is already present, if so remove it
            if self.expression[-1] in ['+', '-', '*', '/']:
                self.expression = self.expression[:-1]
            self.expression += text
            self.display_var.set(self.expression)

def main():
    root = tk.Tk()
    app = MacCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()