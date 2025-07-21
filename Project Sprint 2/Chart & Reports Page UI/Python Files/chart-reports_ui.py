import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class ChartsPage:
    def __init__(self, parent, username, role):
        self.window = tk.Toplevel(parent)
        self.window.title("Reports and Analytics")
        self.window.geometry("600x400")
        self.window.configure(bg="#f0f2f5")

        self.username = username
        self.role = role

        tk.Label(self.window, text=f"{role} Analytics for {username}", font=("Helvetica", 14, "bold"),
                 bg="#f0f2f5").pack(pady=10)

        # Example chart: Food Saved Per Week
        self.create_chart()

        tk.Button(self.window, text="Close", command=self.window.destroy,
                  bg="#e74c3c", fg="white").pack(pady=10)

    def create_chart(self):
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
        food_saved = [30, 45, 60, 50]  # dummy data in kg

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(weeks, food_saved, color="#4a90e2")
        ax.set_title("Food Saved Per Week")
        ax.set_ylabel("Kilograms (kg)")
        ax.set_ylim(0, max(food_saved) + 10)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)
