
import tkinter as tk
from pickup_route_optimizer import PickupRouteOptimizer

class RoutePage:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Pickup Route Optimizer")
        self.window.geometry("500x400")
        self.window.configure(bg="#f0f2f5")

        tk.Label(self.window, text="Optimized Pickup Route", font=("Helvetica", 14, "bold"), bg="#f0f2f5").pack(pady=10)

        # Example locations (can be replaced with dynamic input)
        locations = [
            ("Warehouse", 0, 0),
            ("A", 2, 3),
            ("B", 5, 4),
            ("C", 1, 7),
            ("D", 6, 1)
        ]
        optimizer = PickupRouteOptimizer(locations)
        route = optimizer.optimize_route()
        route_str = " -> ".join(route)
        tk.Label(self.window, text=route_str, font=("Helvetica", 12), bg="#f0f2f5").pack(pady=20)

        tk.Button(self.window, text="Close", command=self.window.destroy, bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)
