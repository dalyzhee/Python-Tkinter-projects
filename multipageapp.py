import tkinter as tk
from tkinter import messagebox

# Main class that calls all the other pages
class MultiPageApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("login System")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Store current user
        self.current_user = None
        
        # Container to stack frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Create all pages
        for F in (LoginPage, RegisterPage, DashboardPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show login page first
        self.show_frame(LoginPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f0f0f0")
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="Login Page", font=("Arial", 24, "bold"), bg="#f0f0f0")
        title_label.pack(pady=30)
        
        #username
        username_label = tk.Label(self, text="Username: ", font=("Arial", 12), bg="#f0f0f0")
        username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)
        
        # Passowrd
        password_label = tk.Label(self, text="Password: ", font=("Arial", 12), bg="#f0f0f0")
        password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self, font=("Arial", 12), width=30, show="*")
        self.password_entry.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        login_button = tk.Button(button_frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        login_button.grid(row=0, column=0, padx=10)
        
        Register_button = tk.Button(button_frame, text="Go to register", command=lambda: controller.show_frame(RegisterPage), bg="#2196F3", fg="white", font=("Arial", 12), width=15)
        Register_button.grid(row=0, column=1, padx=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be more that 6 characters.")
            return
        
        # simulate a successfull login
        self.controller.current_user = username
        messagebox.showinfo("Success", f"Welcome {username}!")
        
        # Go to dashboard
        self.controller.show_frame(DashboardPage)
        
        # clear fields
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e8f5e9")
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="Register Page", font=("Arial", 24, "bold"), bg="#e8f5e9")
        title_label.pack(pady=30)
        
        # Username
        username_label = tk.Label(self, text="Create Username:", font=("Arial", 12), bg="#e8f5e9")
        username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)
        
        # Email
        email_label = tk.Label(self, text="Email:", font=("Arial", 12), bg="#e8f5e9")
        email_label.pack(pady=5)
        
        self.email_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.email_entry.pack(pady=5)
        
        # Password
        password_label = tk.Label(self, text="Create Password:", font=("Arial", 12), bg="#e8f5e9")
        password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self, font=("Arial", 12), width=30, show="*")
        self.password_entry.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self, bg="#e8f5e9")
        button_frame.pack(pady=30)
        
        # Register button
        register_btn = tk.Button(button_frame, text="Register", command=self.register,bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        register_btn.grid(row=0, column=0, padx=10)
        
        # Back to Login button
        login_btn = tk.Button(button_frame, text="Back to Login", command=lambda: controller.show_frame(LoginPage),bg="#f44336", fg="white", font=("Arial", 12), width=15)
        login_btn.grid(row=0, column=1, padx=10)
    
    def register(self):
        """Handle registration"""
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not username or not email or not password:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        if "@" not in email:
            messagebox.showerror("Error", "Invalid email format!")
            return
        
        messagebox.showinfo("Success", f"Account created!\nUsername: {username}\nEmail: {email}")
        
        # Clear fields
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        
        # Go back to login
        self.controller.show_frame(LoginPage)
        
class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1976D2")
        self.controller = controller
        
        # Welcome section
        welcome_frame = tk.Frame(self, bg="#1976D2")
        welcome_frame.pack(pady=30)
        
        welcome_label = tk.Label(welcome_frame, text="Dashboard", font=("Arial", 28, "bold"), bg="#1976D2", fg="white")
        welcome_label.pack()
        
        self.user_label = tk.Label(welcome_frame, text="", font=("Arial", 14), bg="#1976D2", fg="white")
        self.user_label.pack(pady=10)
        
        # Statistics frame
        stats_frame = tk.Frame(self, bg="#1976D2")
        stats_frame.pack(pady=10)
        
        # Sample statistics
        stat1 = tk.Label(stats_frame, text="📊 Tasks: 12", font=("Arial", 14), bg="#1976D2", fg="white")
        stat1.pack(pady=5)
        
        stat2 = tk.Label(stats_frame, text="✅ Completed: 8", font=("Arial", 14), bg="#1976D2", fg="white")
        stat2.pack(pady=5)
        
        stat3 = tk.Label(stats_frame, text="⏳ Pending: 4", font=("Arial", 14), bg="#1976D2", fg="white")
        stat3.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self, bg="#1976D2")
        button_frame.pack(pady=5)
        
        # Profile button
        profile_btn = tk.Button(button_frame, text="View Profile", bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        profile_btn.grid(row=0, column=0, padx=10)
        
        # Settings button
        settings_btn = tk.Button(button_frame, text="Settings", bg="#FF9800", fg="white", font=("Arial", 12), width=15)
        settings_btn.grid(row=0, column=1, padx=10)
        
        # Logout button
        logout_btn = tk.Button(button_frame, text="Logout", command=self.logout, bg="#f44336", fg="white", font=("Arial", 12), width=15)
        logout_btn.grid(row=1, column=0, columnspan=2, pady=10)
    
    def tkraise(self):
        """Update user label when page is shown"""
        if self.controller.current_user:
            self.user_label.config(text=f"Welcome, {self.controller.current_user}!")
        tk.Frame.tkraise(self)
    
    def logout(self):
        """Handle logout"""
        self.controller.current_user = None
        self.controller.show_frame(LoginPage)
        messagebox.showinfo("Logged Out", "You have been logged out!")

class SettingPage(tk.Frame):
    pass

class ProfilePage(tk.Frame):
    pass


if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()