import tkinter as tk
from tkinter import ttk, messagebox

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.expenses = []

        # Title Label
        title_label = tk.Label(self.root, text="Personal Finance Tracker", font=("Helvetica", 18, "bold"), bg="#3498db", fg="white")
        title_label.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill=tk.X)

        tk.Label(input_frame, text="Description:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.desc_entry = ttk.Entry(input_frame, width=25)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Amount ($):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.amount_entry = ttk.Entry(input_frame, width=25)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        add_button = ttk.Button(input_frame, text="Add Expense", command=self.add_expense)
        add_button.grid(row=0, column=2, rowspan=2, padx=10, pady=5)

        # Table Frame
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        columns = ("Description", "Amount ($)")
        self.expense_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        self.expense_table.heading("Description", text="Description")
        self.expense_table.heading("Amount ($)", text="Amount ($)")
        self.expense_table.column("Description", width=300)
        self.expense_table.column("Amount ($)", width=100, anchor=tk.E)
        self.expense_table.pack(fill=tk.BOTH, expand=True)

        # Total Frame
        total_frame = tk.Frame(self.root, padx=10, pady=10)
        total_frame.pack(fill=tk.X)

        tk.Label(total_frame, text="Total Expenses: ", font=("Helvetica", 12)).pack(side=tk.LEFT)
        self.total_label = tk.Label(total_frame, text="$0.00", font=("Helvetica", 12, "bold"), fg="red")
        self.total_label.pack(side=tk.LEFT)

        clear_button = ttk.Button(total_frame, text="Clear All", command=self.clear_all)
        clear_button.pack(side=tk.RIGHT)

    def add_expense(self):
        description = self.desc_entry.get().strip()
        try:
            amount = float(self.amount_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a valid number.")
            return

        if not description:
            messagebox.showerror("Invalid Input", "Description cannot be empty.")
            return

        self.expenses.append((description, amount))
        self.expense_table.insert("", tk.END, values=(description, f"{amount:.2f}"))
        self.update_total()
        self.clear_entries()

    def update_total(self):
        total = sum(amount for _, amount in self.expenses)
        self.total_label.config(text=f"${total:.2f}")

    def clear_entries(self):
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def clear_all(self):
        self.expenses = []
        for item in self.expense_table.get_children():
            self.expense_table.delete(item)
        self.update_total()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
