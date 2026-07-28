import tkinter as tk


class ModernButton(tk.Label):

    def __init__(self, parent, text, command=None, **kwargs):
        self.command = command

        # Premium unified dark colors based on your final preference
        self.BASE_BG = "#1e222b"
        self.HOVER_BG = "#3a3f4d"
        self.CLICK_BG = "#4b5263"
        self.TEXT_COLOR = "#ffffff"

        # Dynamic Auto-Width Calculation strictly set to text length + 2
        dynamic_width = len(text) + 2

        super().__init__(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=self.BASE_BG,
            fg=self.TEXT_COLOR,
            width=dynamic_width,
            height=2,
            justify="center",
            cursor="hand2",
            # Uniformly applying the favorite sunken frame profile to all buttons
            bd=2,
            relief="sunken",
            **kwargs
        )

        # Bind reactive hover, press (click), release, and action events
        self.bind("<Enter>", self._on_hover_enter)
        self.bind("<Leave>", self._on_hover_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_hover_enter(self, event):
        self.config(bg=self.HOVER_BG)

    def _on_hover_leave(self, event):
        self.config(bg=self.BASE_BG)

    def _on_press(self, event):
        self.config(bg=self.CLICK_BG)

    def _on_release(self, event):
        x, y = self.winfo_pointerxy()
        widget_x = self.winfo_rootx()
        widget_y = self.winfo_rooty()
        if widget_x <= x <= widget_x + self.winfo_width() and widget_y <= y <= widget_y + self.winfo_height():
            self.config(bg=self.HOVER_BG)
        else:
            self.config(bg=self.BASE_BG)
            
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

# All buttons now feature your exact favorite structural frame aesthetic side-by-side
btn1 = ModernButton(button_container, "Save Changes", lambda: sample_action("  Saved "))
btn1.pack(side="left", padx=6)

btn2 = ModernButton(button_container, "Confirm and Submit Data", lambda: sample_action("Confirm Button"))
btn2.pack(side="left", padx=6)

btn3 = ModernButton(button_container, "Delete", lambda: sample_action("Delete Button"))
btn3.pack(side="left", padx=6)

btn4 = ModernButton(button_container, "Cancel Process", lambda: sample_action("Cancel Button"))
btn4.pack(side="left", padx=6)

# Force the layout system engine to wrap the window size around the tight contents instantly
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()

