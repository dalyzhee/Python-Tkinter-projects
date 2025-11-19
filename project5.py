import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_counter()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
    

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        update_counter()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    if task_listbox.size() > 0:
        if messagebox.askyesno("Confirm", "Delete all task ?"):
            task_listbox.delete(0, tk.END)
            update_counter()

def update_counter():
    count = task_listbox.size()
    counter_label.config(text=f"Total Task: {count}")

root = tk.Tk()
root.title("Todo app with tkinter")
root.geometry("450x500")
root.config(bg="#2c3e50")

title_label = tk.Label(root, text="Todo-List app with tkinter", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=15)

# input frame
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, font=("Arial", 14), width=25)
task_entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(input_frame, text="Add Task", command=add_task, bg="#27ae60", fg="white", font=("Arial", 12), width=10)
add_btn.pack(side=tk.LEFT, padx=5)

# listbox frame with scrollbar
listbox_frame = tk.Frame(root, bg="#2c3e50")
listbox_frame.pack(padx=10, pady=20)

# Scrollbar
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox widget
task_listbox = tk.Listbox(listbox_frame, font=("Arial", 12), width=40, height=12, selectbackground="#3498db", yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT)

scrollbar.config(command=task_listbox.yview)

# Button frame
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_task, font=("Arial", 11), width=15, bg="#e74c3c", fg="white")
delete_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all, font=("Arial", 11), width=15, bg="#c0392b", fg="white")
clear_button.grid(row=0, column=1, padx=5)

counter_label = tk.Label(root, text="Total Task: 0", font=("Arial", 12), bg="#2c3e50", fg="white")
counter_label.pack(pady=10)

# Bind enter key to add task function
task_entry.bind('<Return>', lambda event: add_task())

root.mainloop()