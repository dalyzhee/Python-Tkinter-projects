import tkinter as tk
from tkinter import messagebox

def show_greeting():
    name = new_entry.get()
    if name.strip():
        greeting = f"hello, {name}! Welcome to kenya."
        result_label.config(text=greeting, fg="green")
    else:
        messagebox.showwarning("Empty field", "Please enter your name!")

def clear_greeting():
    new_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

root = tk.Tk()
root.title("Greating based on user input.")
root.geometry("400x300")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Greating from user input", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# fram for user input
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Enter your name: ", font=("Arial", 12), bg="#f0f0f0")
name_label.grid(row=0, column=0, padx=5)

# entry widget (input widget)
new_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
new_entry.grid(row=0, column=1, padx=5)

# button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# greet button
greet_btn = tk.Button(button_frame, text="Greet Me", command=show_greeting, bg="#4CAF50", fg="white", font=("Arial", 11), width=10)
greet_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_greeting, bg="#f44336", fg="white", font=("Arial", 11), width=10)
clear_btn.grid(row=0, column=1, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", wraplength=350)
result_label.pack(pady=20)


root.mainloop()