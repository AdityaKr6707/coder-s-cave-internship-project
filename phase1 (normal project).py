import tkinter as tk
from tkinter import messagebox, ttk

class ExpenseManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Manager")
        self.balance = {}

        # Configure background color
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.create_widgets()

    def create_widgets(self):
        # Define fonts
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")
        treeview_font = ("Helvetica", 11)

        # Labels and Entry widgets
        self.create_label("Payer:", 0, 0, label_font)
        self.payer_entry = self.create_entry(0, 1, entry_font)

        self.create_label("Amount (₹):", 1, 0, label_font)
        self.amount_entry = self.create_entry(1, 1, entry_font)

        self.create_label("Others involved (comma-separated):", 2, 0, label_font)
        self.users_entry = self.create_entry(2, 1, entry_font)

        # Buttons
        self.create_button("Add Expense", self.add_expense, 3, button_font, "#4CAF50")
        self.create_button("Print Balances", self.print_balance, 4, button_font, "#008CBA")
        self.create_button("Settle Balances", self.settle_up_prompt, 5, button_font, "#f44336")
        self.create_button("Exit", self.root.quit, 6, button_font, "#555555")

        # Treeview for displaying balances
        self.balance_tree = self.create_treeview(7, 0, 2, treeview_font)

    def create_label(self, text, row, column, font):
        tk.Label(self.root, text=text, font=font, bg="#f0f0f0").grid(row=row, column=column, padx=10, pady=10)

    def create_entry(self, row, column, font):
        entry = tk.Entry(self.root, font=font)
        entry.grid(row=row, column=column, padx=10, pady=10)
        return entry

    def create_button(self, text, command, row, font, bg_color):
        tk.Button(self.root, text=text, command=command, font=font, bg=bg_color, fg="white").grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def create_treeview(self, row, column, columnspan, font):
        tree = ttk.Treeview(self.root, columns=('Amount', 'Status'), show='headings', height=10)
        tree.heading('#0', text='Person')
        tree.heading('Amount', text='Amount')
        tree.heading('Status', text='Status')
        tree.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=10, sticky="nsew")

        # Configure treeview font
        style = ttk.Style()
        style.configure('Treeview', font=font)

        return tree

    def add_expense(self):
        payer = self.payer_entry.get().strip()
        amount_str = self.amount_entry.get().strip().replace('₹', '').replace(',', '')
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid amount.")
            return

        users = [user.strip() for user in self.users_entry.get().split(",") if user.strip()]

        if not payer or amount <= 0 or not users:
            messagebox.showwarning("Warning", "Please fill all fields correctly.")
            return

        total_users = len(users) + 1
        split_amount = amount / total_users

        self.update_balance(payer, -amount)

        for user in users:
            self.update_balance(user, split_amount)

        self.clear_entries()
        self.update_balance_tree()

    def update_balance(self, person, amount):
        if person in self.balance:
            self.balance[person] += amount
        else:
            self.balance[person] = amount

    def print_balance(self):
        self.update_balance_tree()

    def settle_up_prompt(self):
        settle_window = tk.Toplevel(self.root)
        settle_window.title("Settle Balances")

        self.create_label("Enter name to settle balances for:", 0, 0, ("Helvetica", 12))
        settle_entry = self.create_entry(0, 1, ("Helvetica", 12))

        self.create_button("Settle", lambda: self.settle_up(settle_entry.get().strip()), 1, ("Helvetica", 12, "bold"), "#008CBA")

    def settle_up(self, person):
        if person in self.balance:
            settle_text = f"Settlements for {person}:\n"
            for other_person, amount in self.balance.items():
                if other_person != person:
                    if amount > 0:
                        settle_text += f"{person} owes {other_person}: ₹{amount:.2f}\n"
                    elif amount < 0:
                        settle_text += f"{other_person} owes {person}: ₹{-amount:.2f}\n"
            messagebox.showinfo("Settlements", settle_text)
        else:
            messagebox.showinfo("No Balances", f"No recorded balances for {person}.")

    def clear_entries(self):
        self.payer_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.users_entry.delete(0, tk.END)

    def update_balance_tree(self):
        # Clear previous items
        for item in self.balance_tree.get_children():
            self.balance_tree.delete(item)

        # Update with current balances
        for person, amount in self.balance.items():
            status = "Owed" if amount != 0 else "Settled"
            color_code = 'green' if amount >= 0 else 'red'
            self.balance_tree.insert('', 'end', text=person, values=(f"₹{amount:.2f}", status), tags=(status,))
            self.balance_tree.tag_configure(status, foreground=color_code)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseManagerGUI(root)
    root.mainloop()

