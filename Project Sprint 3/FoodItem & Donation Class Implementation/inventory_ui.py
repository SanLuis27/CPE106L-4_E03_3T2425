import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from inventory_manager import InventoryManager, FoodItem
from inventory_manager import InventoryManager
from food_donation import FoodItem

class InventoryUI:
    def __init__(self, parent):
        self.manager = InventoryManager()

        self.window = tk.Toplevel(parent)
        self.window.title("Inventory Manager")
        self.window.geometry("600x500")
        self.window.configure(bg="#f0f2f5")

        tk.Label(self.window, text="Inventory Manager", font=("Helvetica", 16, "bold"), bg="#f0f2f5").pack(pady=10)

        # Form inputs
        form_frame = tk.Frame(self.window, bg="#f0f2f5")
        form_frame.pack(pady=10)

        self.name_entry = self.create_labeled_entry(form_frame, "Food Name:")
        self.category_entry = self.create_labeled_entry(form_frame, "Category:")
        self.quantity_entry = self.create_labeled_entry(form_frame, "Quantity:")
        self.days_entry = self.create_labeled_entry(form_frame, "Expires in (days):")

        tk.Button(self.window, text="Add Food Item", command=self.add_food_item,
                  bg="#27ae60", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

        # Inventory list
        self.listbox = tk.Listbox(self.window, width=70)
        self.listbox.pack(pady=10)

        tk.Button(self.window, text="Mark as Delivered", command=self.mark_selected_delivered,
                  bg="#e67e22", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)

        tk.Button(self.window, text="Refresh List", command=self.refresh_list,
                  bg="#2980b9", fg="white", font=("Helvetica", 10, "bold")).pack(pady=5)

        tk.Button(self.window, text="Close", command=self.window.destroy,
                  bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

        self.refresh_list()

    def create_labeled_entry(self, parent, label_text):
        frame = tk.Frame(parent, bg="#f0f2f5")
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, bg="#f0f2f5").pack(side="left", padx=5)
        entry = tk.Entry(frame)
        entry.pack(side="left", padx=5)
        return entry

    def add_food_item(self):
        name = self.name_entry.get()
        category = self.category_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            days = int(self.days_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity and Days must be numbers.")
            return

        expiration_date = datetime.now().date() + timedelta(days=days)
        item = FoodItem(name, category, quantity, expiration_date)
        self.manager.add_item(item)
        messagebox.showinfo("Success", "Food item added to inventory.")
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        available_items = self.manager.get_available_items()
        for item in available_items:
            display = f"{item.id[:6]} | {item.name} ({item.category}) - {item.quantity} units, Expires: {item.expiration_date}"
            self.listbox.insert(tk.END, display)

    def mark_selected_delivered(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to mark as delivered.")
            return
        selected_text = self.listbox.get(selection[0])
        item_id_prefix = selected_text.split("|")[0].strip()
        # Find item by ID prefix
        for item in self.manager.get_available_items():
            if item.id.startswith(item_id_prefix):
                self.manager.mark_item_as_delivered(item.id)
                messagebox.showinfo("Marked Delivered", f"{item.name} marked as delivered.")
                self.refresh_list()
                return
        messagebox.showerror("Error", "Item not found.")

