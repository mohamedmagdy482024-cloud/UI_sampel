import tkinter as tk


class ModernButton(tk.Label):

    def __init__(self, parent, text, btn_type="primary", command=None, **kwargs):
        self.btn_type = btn_type
        self.command = command

        # Modern UI Color Palette matched with your design system
        self.colors = {
            "primary": {"bg": "#2196f3", "hover": "#1e88e5", "fg": "#ffffff"},
            "success": {"bg": "#4caf50", "hover": "#43a047", "fg": "#ffffff"},
            "danger": {"bg": "#f44336", "hover": "#e53935", "fg": "#ffffff"},
            "outline": {"bg": "#1e222b", "hover": "#3a3f4d", "fg": "#ffffff", "border": "#4b5263"}
        }

        current_colors = self.colors.get(self.btn_type, self.colors["primary"])

        # Dynamic Auto-Width Calculation function based on character length + padding safety units
        # This keeps the button size wrapping tightly and exactly around the internal text string
        dynamic_width = len(text) + 2

        super().__init__(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=current_colors["bg"],
            fg=current_colors["fg"],
            width=dynamic_width,
            height=2,
            justify="center",
            cursor="hand2",
            bd=1 if "border" in current_colors else 0,
            relief="flat",
            **kwargs
        )

        # Apply specific configuration for outline styles manually
        if "border" in current_colors:
            self.config(highlightbackground=current_colors["border"], highlightthickness=1)

        # Bind reactive hover updates and click actions
        self.bind("<Enter>", self._on_hover_enter)
        self.bind("<Leave>", self._on_hover_leave)
        self.bind("<Button-1>", self._on_click)

    def _on_hover_enter(self, event):
        current_colors = self.colors.get(self.btn_type, self.colors["primary"])
        self.config(bg=current_colors["hover"])

    def _on_hover_leave(self, event):
        current_colors = self.colors.get(self.btn_type, self.colors["primary"])
        self.config(bg=current_colors["bg"])

    def _on_click(self, event):
        if self.command:
            self.command()


def sample_action(btn_name):
    print(f"Action triggered from: {btn_name}")


# Initialize the main window
root = tk.Tk()
root.title("Modern Dark Dynamic Buttons")
root.configure(bg="#1e222b")

# Container frame to center buttons beautifully
button_container = tk.Frame(root, bg="#1e222b")
button_container.pack(padx=20, pady=20)

# Rendering 4 different button designs with dynamic text-wrapped widths
btn1 = ModernButton(button_container, "Save Changessssssssssss", "primary", lambda: sample_action("Save Button"))
btn1.pack(side="left", padx=6)

btn2 = ModernButton(button_container, "Confirm and Submit Data", "success", lambda: sample_action("Success Button"))
btn2.pack(side="left", padx=6)

btn3 = ModernButton(button_container, "Delete", "danger", lambda: sample_action("Delete Button"))
btn3.pack(side="left", padx=6)

btn4 = ModernButton(button_container, "Cancel Process", "outline", lambda: sample_action("Cancel Button"))
btn4.pack(side="left", padx=6)

# Force the layout system engine to wrap the window size around the tight contents instantly
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()

