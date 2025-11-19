import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalied Expression")
        clear_display()
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))
def clear_display():
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Calclator with tkinter")
root.geometry("330x470")
root.resizable(False, False)

# title_label = tk.Label(root, text="Calculator with Tkinter", font=("Arial", 20, "bold"))
# title_label.pack(pady=10)

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, font=("Arial", 16), width=5, height=2, command=calculate, bg="#4CAF50", fg="white")
    else:
        btn = tk.Button(root, text=button, font=("Arial", 16), width=5, height=2, command=lambda b=button: button_click(b), bg="#e0e0e0")
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1
        
clear_button = tk.Button(root, text="Clear", font=("Arial", 16), width=23, height=2, command=clear_display, bg="#f44336", fg="white")
clear_button.grid(row=row,column=0, columnspan=4, padx=2, pady=2)
root.mainloop()