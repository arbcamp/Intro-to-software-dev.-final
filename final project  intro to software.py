import tkinter as tk
from tkinter import messagebox

class FitnessApp(tk.Tk):
    """
    Main application window for Fitness Tracker.
    """
    def __init__(self):
        """
        Initializes the main application window.
        """
        super().__init__()
        self.title("Fitness Tracker")
        self.geometry("600x400")
        self.configure(bg="green")

        # Create welcome label
        self.label1 = tk.Label(self, text="Welcome to Fitness Tracker", bg="green", fg="white", font=('Arial', 16))
        self.label1.pack(pady=10)

        # Button to open tracking stats window
        self.button1 = tk.Button(self, text="Track Stats", command=self.open_track_stats)
        self.button1.pack(pady=5)

        # Exit button
        self.button_exit = tk.Button(self, text="Exit", command=self.quit)
        self.button_exit.pack(pady=5)

    def open_track_stats(self):
        """
        Opens the window for tracking fitness stats.
        """
        self.withdraw()
        TrackStatsWindow(self)

class TrackStatsWindow(tk.Toplevel):
    """
    Window for tracking fitness stats.
    """
    def __init__(self, master):
        """
        Initializes the window for tracking stats.
        """
        super().__init__(master)
        self.title("Track Stats")
        self.geometry("700x400")
        self.configure(bg="green")

        # Initialize running totals
        self.total_calories = 0.0
        self.total_steps = 0
        self.total_protein = 0.0
        self.total_carbs = 0.0

        # Create a main frame to hold input and total side-by-side
        self.main_frame = tk.Frame(self, bg="green")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left frame for entries
        self.left_frame = tk.Frame(self.main_frame, bg="green")
        self.left_frame.pack(side="left", fill="y", padx=10)

        # Right frame for totals display
        self.right_frame = tk.Frame(self.main_frame, bg="lightgray", width=200, height=300, relief="sunken", bd=2)
        self.right_frame.pack(side="right", fill="y", padx=10)
        self.right_frame.pack_propagate(False)

        # Entry fields
        self.create_labeled_entry("Calories:", "calories_entry")
        self.create_labeled_entry("Steps:", "steps_entry")
        self.create_labeled_entry("Protein (g):", "protein_entry")
        self.create_labeled_entry("Carbs (g):", "carbs_entry")

        # Buttons
        self.submit_button = tk.Button(self.left_frame, text="Submit", command=self.submit_stats)
        self.submit_button.pack(pady=5)

        self.back_button = tk.Button(self.left_frame, text="Back to Main Menu", command=self.back_to_main)
        self.back_button.pack(pady=5)

        # Label in right panel to show totals
        self.totals_label = tk.Label(self.right_frame, text=self.get_totals_text(), bg="lightgray", font=('Arial', 12), justify="left")
        self.totals_label.pack(pady=10)

    def create_labeled_entry(self, label_text, attr_name):
        """
        Creates a label and entry field in the left frame.
        """
        label = tk.Label(self.left_frame, text=label_text, bg="green", fg="white")
        label.pack()
        entry = tk.Entry(self.left_frame)
        entry.pack()
        setattr(self, attr_name, entry)

    def submit_stats(self):
        """
        Submits and adds to running totals, updates right panel.
        """
        try:
            calories = float(self.calories_entry.get())
            steps = int(self.steps_entry.get())
            protein = float(self.protein_entry.get())
            carbs = float(self.carbs_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values in all fields.")
            return

        # Update totals
        self.total_calories += calories
        self.total_steps += steps
        self.total_protein += protein
        self.total_carbs += carbs

        # Update totals display
        self.totals_label.config(text=self.get_totals_text())

        # Clear inputs
        self.clear_entries()

        messagebox.showinfo("Success", "Stats submitted!")

    def clear_entries(self):
        """
        Clears all the input fields.
        """
        self.calories_entry.delete(0, tk.END)
        self.steps_entry.delete(0, tk.END)
        self.protein_entry.delete(0, tk.END)
        self.carbs_entry.delete(0, tk.END)

    def get_totals_text(self):
        """
        Returns formatted string of totals.
        """
        return (f"Running Totals:\n"
                f"Calories: {self.total_calories:.1f}\n"
                f"Steps: {self.total_steps}\n"
                f"Protein: {self.total_protein:.1f} g\n"
                f"Carbs: {self.total_carbs:.1f} g")

    def back_to_main(self):
        """
        Returns to the main menu.
        """
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    root = FitnessApp()
    root.mainloop()
