import tkinter as tk
from tkinter import messagebox
from login_bl import LoginManager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from route_ui import RoutePage
from inventory_ui import InventoryUI


class ChartsPage:
    def __init__(self, parent, username, role):
        self.window = tk.Toplevel(parent)
        self.window.title("Reports and Analytics")
        self.window.geometry("900x700")
        self.window.configure(bg="#f0f2f5")

        self.username = username
        self.role = role

        tk.Label(self.window, text=f"{role} Analytics for {username}", font=("Helvetica", 14, "bold"),
                 bg="#f0f2f5").pack(pady=10)

        self.create_all_charts()

        tk.Button(self.window, text="Close", command=self.window.destroy,
                  bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

    def create_all_charts(self):
        # Chart 1: Food Saved Per Week (Bar)
        fig1, ax1 = plt.subplots(figsize=(4.5, 3))
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
        food_saved = [120, 180, 140, 200]  # dummy data
        ax1.bar(weeks, food_saved, color="#4a90e2")
        ax1.set_title("Food Saved Per Week")
        ax1.set_ylabel("Kilograms (kg)")
        self.embed_chart(fig1)

        # Chart 2: Donor Distribution (Pie)
        fig2, ax2 = plt.subplots(figsize=(4.5, 3))
        donor_sources = ["Restaurants", "Groceries", "Individuals"]
        donor_counts = [15, 10, 5]
        ax2.pie(donor_counts, labels=donor_sources, autopct='%1.1f%%', startangle=90)
        ax2.set_title("Donor Distribution")
        self.embed_chart(fig2)

        # Chart 3: Delivery Progress (Line)
        fig3, ax3 = plt.subplots(figsize=(4.5, 3))
        days = ["Day 1", "Day 2", "Day 3", "Day 4"]
        deliveries = [5, 12, 20, 28]
        ax3.plot(days, deliveries, marker='o', color="#27ae60")
        ax3.set_title("Delivery Progress Over Time")
        ax3.set_ylabel("Deliveries Completed")
        self.embed_chart(fig3)

    def embed_chart(self, fig):
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)


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
        import requests
        try:
            response = requests.post(
                "http://127.0.0.1:8000/login",
                json={"username": username, "password": password},
                timeout=3
            )
            if response.status_code == 200:
                messagebox.showinfo("Login Success", f"Welcome, {username}!")
                self.select_role(username)
            else:
                messagebox.showerror("Login Failed", response.json().get("detail", "Invalid username or password."))
        except Exception as e:
            # Fallback to local logic if API is unreachable
            if self.manager.authenticate_user(username, password):
                messagebox.showinfo("Login Success", f"Welcome, {username}!")
                self.select_role(username)
            else:
                messagebox.showerror("Login Failed", f"Invalid username or password. (API unreachable: {e})")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        import requests
        try:
            response = requests.post(
                "http://127.0.0.1:8000/register",
                json={"username": username, "password": password},
                timeout=3
            )
            if response.status_code == 200:
                messagebox.showinfo("Registration Success", "User registered successfully.")
            else:
                messagebox.showerror("Registration Failed", response.json().get("detail", "Username already exists."))
        except Exception as e:
            # Fallback to local logic if API is unreachable
            if self.manager.register_user(username, password):
                messagebox.showinfo("Registration Success", "User registered successfully.")
            else:
                messagebox.showerror("Registration Failed", f"Username already exists. (API unreachable: {e})")

    def select_role(self, username):
        self.role_window = tk.Toplevel()
        self.role_window.title("Select Your Role")
        self.role_window.geometry("300x200")
        self.role_window.configure(bg=self.colors[self.theme]["bg"])

        tk.Label(self.role_window, text="Choose Your Role", font=("Helvetica", 14),
                 bg=self.colors[self.theme]["bg"], fg=self.colors[self.theme]["fg"]).pack(pady=20)

        tk.Button(self.role_window, text="Donor", font=("Helvetica", 10, "bold"),
                  bg="#4a90e2", fg="white",
                  command=lambda: self.open_dashboard(username, "Donor")).pack(pady=10)

        tk.Button(self.role_window, text="Recipient", font=("Helvetica", 10, "bold"),
                  bg="#27ae60", fg="white",
                  command=lambda: self.open_dashboard(username, "Recipient")).pack(pady=10)

        # Back button to return to login screen
        tk.Button(self.role_window, text="Back", font=("Helvetica", 10, "bold"),
                  bg="#b2bec3", fg="black",
                  command=self.role_window.destroy).pack(pady=10)

    def open_dashboard(self, username, role="User"):
        self.root.withdraw()
        self.role_window.destroy()

        dashboard = tk.Toplevel()
        dashboard.title(f"{role} Dashboard - {username}")
        dashboard.geometry("400x500")
        dashboard.configure(bg=self.colors[self.theme]["bg"])

        greeting = f"Welcome, {username}!\nRole: {role}"
        tk.Label(dashboard, text=greeting, font=("Helvetica", 14),
                 bg=self.colors[self.theme]["bg"], fg=self.colors[self.theme]["fg"]).pack(pady=20)

        tk.Button(dashboard, text="View Charts & Reports",
                  command=lambda: ChartsPage(self.root, username, role),
                  bg="#7ed6df", fg="black").pack(pady=10)

        tk.Button(dashboard, text="Pickup Route Optimizer",
                  command=lambda: RoutePage(self.root),
                  bg="#f6e58d", fg="black").pack(pady=10)

        tk.Button(dashboard, text="Manage Inventory",
                  command=lambda: InventoryUI(self.root),
                  bg="#badc58", fg="black").pack(pady=10)

        # Analytics Manager Button
        import sys
        import os
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        if parent_dir not in sys.path:
            sys.path.append(parent_dir)
        from analytics_ui import AnalyticsPage
        tk.Button(dashboard, text="Analytics Manager",
                  command=lambda: AnalyticsPage(self.root),
                  bg="#4a90e2", fg="white").pack(pady=10)

        # Back button to return to role selection
        def back_to_role():
            dashboard.destroy()
            self.root.deiconify()
            self.select_role(username)
        tk.Button(dashboard, text="Back", font=("Helvetica", 10, "bold"),
                  bg="#b2bec3", fg="black",
                  command=back_to_role).pack(pady=10)

        tk.Button(dashboard, text="Logout",
                  command=lambda: self.logout(dashboard),
                  bg="#e74c3c", fg="white").pack(pady=10)

    def logout(self, dashboard_window):
        dashboard_window.destroy()
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
