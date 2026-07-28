import tkinter as tk
from tkinter import ttk


class CheckableComboBox(ttk.Combobox):

    def __init__(self, parent, options, **kwargs):
        # Calculate initial tight width based on the longest single item
        self.initial_width = max(len(opt) for opt in options) + 4

        # Initialize native Combobox as readonly to match your exact UI style
        super().__init__(
            parent, state="readonly", width=self.initial_width, **kwargs
        )

        self.options = options
        self.choices = {}

        # FIXED: We use the clear, native checkbuttons just like the original code you liked
        self.menu = tk.Menu(self, tearoff=0)

        for option in self.options:
            self.choices[option] = tk.BooleanVar(value=False)
            self.menu.add_checkbutton(
                label=option,
                variable=self.choices[option],
                onvalue=True,
                offvalue=False,
                command=self.update_display_text,
                background="#1e222b",  # Dark background for the menu list
                foreground="#ffffff",  # White text for options
                selectcolor="#3b82f6",  # Blue background for checked indicators
                activebackground="#2d3139",  # Highlight color on mouse hover
                activeforeground="#ffffff",
            )

        # Intercept the default left-click to display our custom menu instead
        self.bind("<Button-1>", self.show_menu)
        self.set("Select Items")

    def show_menu(self, event):
        """Displays the custom dark checkbox menu directly below the combobox container."""
        self.menu.post(self.winfo_rootx(), self.winfo_rooty() + self.winfo_height())
        return "break"  # Block native dropdown menu execution

    def update_display_text(self):
        """Updates display text and stretches the width dynamically when items are checked."""
        checked_items = [
            opt for opt, var in self.choices.items() if var.get() is True
        ]

        # Temporarily switch to normal state to allow code to modify the field text
        self.config(state="normal")

        if checked_items:
            display_text = ", ".join(checked_items)
            self.delete(0, tk.END)
            self.insert(0, display_text)

            # Update the width dynamically so long joined text is never truncated
            dynamic_width = len(display_text) + 2
            self.config(width=dynamic_width)
        else:
            self.delete(0, tk.END)
            self.insert(0, "Select Items")
            self.config(width=self.initial_width)

        self.config(state="readonly")


# 1. Main Window Setup
root = tk.Tk()
root.title("Dark Theme Checkbox Combo Box")
root.geometry("380x250")

# Setup dark theme colors with a bright, crisp border color
DARK_BG = "#1e222b"
BRIGHT_BORDER = "#555d6b"  # Much brighter grey for highly visible borders
TEXT_COLOR = "#ffffff"

root.config(bg=DARK_BG)

# 2. FIXED: Apply a clear, bright border around the pop-up menu container itself
root.option_add("*Menu.borderWidth", 1)
root.option_add("*Menu.borderColor", BRIGHT_BORDER)
root.option_add("*Menu.relief", "solid")

# 3. Configure ttk Styles to apply the sharp and clear border appearance for the box
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground=DARK_BG,  # Text area background
    background=DARK_BG,  # Arrow button background (blends inner line)
    foreground=TEXT_COLOR,  # White text
    bordercolor=BRIGHT_BORDER,  # Sharp visible outer border color
    lightcolor=DARK_BG,  # Clears interior splitting highlights
    darkcolor=DARK_BG,  # Clears interior shadows
    arrowcolor=TEXT_COLOR,  # Clean sharp white arrow triangle
    borderwidth=1,  # Sets explicit border line weight
    padding=6,
)

style.map(
    "TCombobox",
    fieldbackground=[("readonly", DARK_BG)],
    foreground=[("readonly", TEXT_COLOR)],
    background=[("readonly", DARK_BG)],
    bordercolor=[
        ("focus", "#3b82f6"),
        ("active", BRIGHT_BORDER),
    ],
)

# 4. Initialize and position the checkbox combo box element
items_list = ["Item 1", "Item 2", "Item 3"]
combo = CheckableComboBox(root, options=items_list)
combo.pack(pady=60)

root.mainloop()

