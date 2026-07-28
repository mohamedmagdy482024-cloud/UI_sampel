import tkinter as tk


class ModernRadioButton(tk.Frame):

    def __init__(self, parent, text, variable, value, command=None, **kwargs):
        super().__init__(parent, bg="#1e222b", **kwargs)
        self.variable = variable
        self.value = value
        self.command = command

        # Modern Hex Colors matching your Combobox theme
        self.DARK_BG = "#1e222b"
        self.LIGHT_DARK_BG = "#2d3139"
        self.TEXT_COLOR = "#ffffff"
        self.ACCENT_BLUE = "#2196f3"  # Vibrant blue indicator color

        # Custom Canvas to draw perfect pixel-crisp vector circles
        self.canvas = tk.Canvas(
            self,
            width=20,
            height=20,
            bg=self.DARK_BG,
            highlightthickness=0,
            cursor="hand2",
        )
        self.canvas.pack(side="left")

        # Label text next to the circle indicator
        self.label = tk.Label(
            self,
            text=text,
            font=("Arial", 11),
            bg=self.DARK_BG,
            fg=self.TEXT_COLOR,
            cursor="hand2",
        )
        self.label.pack(side="left", padx=10)

        # Bind click events to both the circle and the text label
        self.canvas.bind("<Button-1>", self._on_click)
        self.label.bind("<Button-1>", self._on_click)

        # Track changes to redraw the selected states immediately
        self.variable.trace_add("write", self._update_state)
        self._update_state()

    def _on_click(self, event):
        self.variable.set(self.value)
        if self.command:
            self.command()

    def _update_state(self, *args):
        self.canvas.delete("all")
        if self.variable.get() == self.value:
            # Selected state: Crisp glowing blue outer ring and interior dot
            self.canvas.create_oval(
                2, 2, 18, 18, outline=self.ACCENT_BLUE, width=2
            )
            self.canvas.create_oval(
                6, 6, 14, 14, fill=self.ACCENT_BLUE, outline=self.ACCENT_BLUE
            )
        else:
            # Unselected state: Soft dark gray ring
            self.canvas.create_oval(
                2, 2, 18, 18, outline=self.LIGHT_DARK_BG, width=2
            )


def on_theme_change():
    print(f"Selected Theme: {selected_theme.get()}")


# Initialize the main window
root = tk.Tk()
root.title("Dark Theme Radio Buttons")
root.geometry("300x250")

# Matching dark theme background color
DARK_BG = "#1e222b"
TEXT_COLOR = "#ffffff"
root.configure(bg=DARK_BG)

# Title Label for the group
title_label = tk.Label(
    root,
    text="Color theme",
    font=("Arial", 12, "bold"),
    bg=DARK_BG,
    fg=TEXT_COLOR,
)
title_label.pack(anchor="w", padx=40, pady=(30, 10))

# Declare the tracking variable for the radio buttons
selected_theme = tk.StringVar(value="Red")

# Define the options to create
themes = ["Red", "Green", "Blue", "Purple"]

# Create and position each custom modern radio button layout
for theme in themes:
    radio_btn = ModernRadioButton(
        root,
        text=theme,
        variable=selected_theme,
        value=theme,
        command=on_theme_change,
    )
    radio_btn.pack(anchor="w", padx=40, pady=5)

# Start the application loop
root.mainloop()

