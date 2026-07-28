import tkinter as tk
from tkinter import ttk


class CheckableComboBox(ttk.Combobox):

    def __init__(self, parent, options, **kwargs):
        # Calculate initial tight width based on the longest single item
        self.initial_width = max(len(opt) for opt in options) + 6

        # Initialize native Combobox as readonly
        super().__init__(
            parent, state="readonly", width=self.initial_width, **kwargs
        )

        self.options = options
        self.choices = {}

        # Create a custom pop-up menu layer to hold the items
        self.menu = tk.Menu(self, tearoff=0)

        for option in self.options:
            self.choices[option] = tk.BooleanVar(value=False)
            
            # FIXED: Clear text-based border [  ] that is highly visible in dark mode
            initial_label = f"[  ]  {option}"
            
            self.menu.add_command(
                label=initial_label,
                command=lambda opt=option: self.toggle_item(opt),
                background="#1e222b",  # Dark background for the menu list
                foreground="#ffffff",  # White text for options
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

    def toggle_item(self, option):
        """Toggles the state of an item and updates its visual icon in the menu."""
        current_state = self.choices[option].get()
        self.choices[option].set(not current_state)
        
        index = self.options.index(option)
        
        # FIXED: Brings back the crisp original checkmark (✓) with a clear frame
        if self.choices[option].get():
            new_label = f"[ ✓ ]  {option}"
            self.menu.entryconfigure(
                index, 
                label=new_label, 
                foreground="#3b82f6"  # Applies the beautiful original blue color only to the checked item
            )
        else:
            new_label = f"[  ]  {option}"
            self.menu.entryconfigure(
                index, 
                label=new_label, 
                foreground="#ffffff"  # Resets to default white when unchecked
            )
        
        # Update the main text entry field
        self.update_display_text()

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

# 2. Configure ttk Styles to apply the sharp and clear border appearance
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

# 3. Initialize and position the checkbox combo box element
items_list = ["Item 1", "Item 2", "Item 3"]
combo = CheckableComboBox(root, options=items_list)
combo.pack(pady=60)

root.mainloop()

