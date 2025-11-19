# import library
import tkinter as tk
# create main window
root = tk.Tk()
# add window title
root.title("First project with tkinter")
# window size
root.geometry("400x300")
# add label widget
label = tk.Label(root, text="This is my first tkinter app", font=("Arial", 24))
label.pack(pady=50)
# create main event loop
root.mainloop()