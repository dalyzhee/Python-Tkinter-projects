import tkinter as tk
from tkinter import messagebox

def convert_temp():
    try:
        temp = input_entry.get()
        result = ((int(temp) - 32) * 5) / 9
        result = round(result, 3)
        input_entry.delete(0, tk.END)
        display_label.config(text=f"{temp} degrees is equal to {result} Celsius.")
    except ValueError:
        messagebox.showwarning("Warning", "Only integer number are allowed")
        input_entry.delete(0, tk.END)

def clear_input():
    input_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Temp coversion using tkinter")
root.geometry("400x300")

# title label
title_label = tk.Label(root, text="Temparature conversion with tkinter", font=("Arial", 15, "bold"))
title_label.pack(pady=10)

# input using entry
input_entry = tk.Entry(root, font=("Arial", 15), width=20)
input_entry.pack(pady=15)

# Button frames
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# buttons
convert_button = tk.Button(button_frame, text="Convert", font=("Arial", 10), width=10, command=convert_temp, bg="red", fg="white")
convert_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 10), width=10, command=clear_input, bg="red", fg="white")
clear_button.grid(row=0, column=1, padx=5)

# display label
display_label = tk.Label(root, text="0 degrees to celcious is 0", font=("Arial", 15))
display_label.pack(pady=10)

root.mainloop()