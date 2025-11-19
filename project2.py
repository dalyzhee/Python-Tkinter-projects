import tkinter as tk

def increment_counter():
    global count
    count += 1
    label.config(text=f"Count: {count}")

def reset_counter():
    global count
    count = 0
    label.config(text=f"Count: {count}")

root = tk.Tk()
root.title("Click Counter")
root.geometry("300x200")

count = 0

# label
title_label = tk.Label(root, text="Button counter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# counter display
label = tk.Label(root, text=f"count: {count}", font=("Arial", 20))
label.pack(pady=20)

# increment button
increment_button = tk.Button(root, text="Click me!", command=increment_counter, bg="lightblue", fg="black", font=("Arial", 12))
increment_button.pack(pady=5)

# reset button
reset_button = tk.Button(root, text="Reset", command=reset_counter, bg="lightcoral", fg="black", font=("Arial", 12))
reset_button.pack(pady=5)
root.mainloop()