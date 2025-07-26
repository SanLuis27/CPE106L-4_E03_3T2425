import tkinter as tk
from analytics_controller import AnalyticsController

class AnalyticsPage:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Analytics Manager")
        self.window.geometry("500x400")
        self.controller = AnalyticsController()

        tk.Label(self.window, text="Analytics Manager", font=("Helvetica", 14, "bold"), bg="#f0f2f5").pack(pady=10)
        tk.Button(self.window, text="Show Analytics Summary", command=self.show_summary, bg="#4a90e2", fg="white").pack(pady=10)
        self.output_label = tk.Label(self.window, text="", bg="#f0f2f5")
        self.output_label.pack(pady=10)
        self.window.configure(bg="#f0f2f5")

    def show_summary(self):
        # Example data source
        data_source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        summary = self.controller.model.get_summary() if self.controller.model.data else None
        if not summary:
            self.controller.model.load_data(data_source)
            summary = self.controller.model.get_summary()
        text = f"Total records: {summary['count']}\nSample data: {summary['sample']}"
        self.output_label.config(text=text)
