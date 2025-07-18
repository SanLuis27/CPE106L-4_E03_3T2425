import tkinter as tk
from tkinter import messagebox
from login_bl import LoginManager
 
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RePlate Login")
        self.root.geometry("400x500")
        self.root.minsize(360, 420)
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f2f5")
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.fullscreen = False
 
        self.manager = LoginManager()
        self.theme = "light"
        self.colors = {
            "light": {"bg": "#f0f2f5", "fg": "#333", "entry_bg": "white", "button": "#4a90e2"},
            "dark": {"bg": "#2c3e50", "fg": "#ecf0f1", "entry_bg": "#34495e", "button": "#2980b9"}
        }
 
        self.fade_in()
        self.build_ui()
 
    def fade_in(self):
        for i in range(0, 11):
            self.root.attributes("-alpha", i / 10)
            self.root.update()
            self.root.after(30)
 
    def build_ui(self):
        self.container = tk.Frame(self.root, bg=self.colors[self.theme]["entry_bg"])
        self.container.pack(expand=True, fill="both", padx=40, pady=40)
 
        tk.Label(self.container, text="RePlate", font=("Helvetica", 22, "bold"),
                 bg=self.colors[self.theme]["entry_bg"], fg=self.colors[self.theme]["fg"]).pack(pady=(30, 10))
 
        self.username_entry = self.create_labeled_entry("👤", "Username")
        self.password_entry = self.create_labeled_entry("🔒", "Password", show="*")
 
        self.create_button("Login", self.login, self.colors[self.theme]["button"]).pack(pady=(10, 5))
        self.create_button("Register", self.register, "#7ed6df").pack(pady=(0, 10))
 
        self.dark_mode_btn = tk.Button(
            self.container,
            text="🌙 Toggle Dark Mode",
            command=self.toggle_theme,
            bg=self.colors[self.theme]["entry_bg"],
            fg=self.colors[self.theme]["fg"],
            activebackground=self.colors[self.theme]["entry_bg"],
            highlightthickness=0,
            bd=0,
            cursor="hand2"
        )
        self.dark_mode_btn.pack()
 
    def create_labeled_entry(self, icon, placeholder, show=None):
        frame = tk.Frame(self.container, bg=self.colors[self.theme]["entry_bg"])
        frame.pack(pady=10, padx=20, fill="x")
 
        tk.Label(frame, text=icon, font=("Helvetica", 12), bg=self.colors[self.theme]["entry_bg"],
                 fg=self.colors[self.theme]["fg"]).pack(side="left", padx=5)
 
        entry = tk.Entry(frame, font=("Helvetica", 11), bd=0, relief="flat", fg=self.colors[self.theme]["fg"],
                         bg=self.colors[self.theme]["entry_bg"], insertbackground=self.colors[self.theme]["fg"],
                         show=show)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, placeholder))
        entry.bind("<FocusOut>", lambda e: self.add_placeholder(entry, placeholder))
        entry.pack(side="left", fill="x", expand=True)
        return entry
 
    def create_button(self, text, command, color):
        return tk.Button(self.container, text=text, command=command,
                         font=("Helvetica", 10, "bold"), bg=color, fg="white",
                         activebackground="#2c3e50", relief="flat", bd=0,
                         height=2, width=25, cursor="hand2")
 
    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
 
    def add_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
 
    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.root.configure(bg=self.colors[self.theme]["bg"])
        self.container.configure(bg=self.colors[self.theme]["entry_bg"])
        for widget in self.container.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label):
                widget.configure(bg=self.colors[self.theme]["entry_bg"], fg=self.colors[self.theme]["fg"])
            elif isinstance(widget, tk.Button):
                widget.configure(bg=self.colors[self.theme]["entry_bg"], fg=self.colors[self.theme]["fg"])
        self.dark_mode_btn.configure(
            bg=self.colors[self.theme]["entry_bg"],
            fg=self.colors[self.theme]["fg"],
            activebackground=self.colors[self.theme]["entry_bg"]
        )
 
    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
 
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.manager.authenticate_user(username, password):
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.open_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
 
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.manager.register_user(username, password):
            messagebox.showinfo("Registration Success", "User registered successfully.")
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")
 
    def open_dashboard(self, username):
        self.root.withdraw()
        dashboard = tk.Toplevel()
        dashboard.title(f"{username}'s Dashboard")
        dashboard.geometry("400x300")
        dashboard.configure(bg=self.colors[self.theme]["bg"])
 
        tk.Label(dashboard, text=f"Welcome, {username}!", font=("Helvetica", 14),
                 bg=self.colors[self.theme]["bg"], fg=self.colors[self.theme]["fg"]).pack(pady=20)
        tk.Button(dashboard, text="Logout", command=lambda: self.logout(dashboard),
                  bg="#e74c3c", fg="white").pack(pady=10)
 
    def logout(self, dashboard_window):
        dashboard_window.destroy()
        self.root.deiconify()
 
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
