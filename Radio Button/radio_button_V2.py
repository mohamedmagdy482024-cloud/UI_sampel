import tkinter as tk


class ModernRadioButton(tk.Frame):

    def __init__(self, parent, text, variable, value, command=None, **kwargs):
        super().__init__(parent, bg="#1e222b", **kwargs)
        self.variable = variable
        self.value = value
        self.command = command

        # Precision Theme Colors
        self.DARK_BG = "#1e222b"
        self.LIGHT_DARK_BG = "#2d3139"
        self.TEXT_COLOR = "#ffffff"
        self.ACCENT_BLUE = "#2196f3"  # Premium modern blue

        # Canvas container with a perfectly square bounding box
        self.canvas = tk.Canvas(
            self,
            width=20,
            height=20,
            bg=self.DARK_BG,
            highlightthickness=0,
            cursor="hand2",
        )
        self.canvas.pack(side="left")

        # Clean typography alignment
        self.label = tk.Label(
            self,
            text=text,
            font=("Arial", 11),
            bg=self.DARK_BG,
            fg=self.TEXT_COLOR,
            cursor="hand2",
        )
        self.label.pack(side="left", padx=12)

        # Event triggers
        self.canvas.bind("<Button-1>", self._on_click)
        self.label.bind("<Button-1>", self._on_click)

        # Reactive structural binding
        self.variable.trace_add("write", self._update_state)
        self._update_state()

    def _on_click(self, event):
        self.variable.set(self.value)
        if self.command:
            self.command()

    def _update_state(self, *args):
        self.canvas.delete("all")

        if self.variable.get() == self.value:
            # LAYERED VECTOR TRICK FOR PERFECT SMOOTHNESS
            # Step 1: Draw the solid outer accent circle
            self.canvas.create_oval(
                2, 2, 18, 18, fill=self.ACCENT_BLUE, outline=self.ACCENT_BLUE
            )
            # Step 2: Mask the center with a smaller background-colored circle to form a ring
            self.canvas.create_oval(
                4, 4, 16, 16, fill=self.DARK_BG, outline=self.DARK_BG
            )
            # Step 3: Insert the precise central core glowing dot
            self.canvas.create_oval(
                7,
                7,
                13,
                13,
                fill=self.ACCENT_BLUE,
                outline=self.ACCENT_BLUE,
            )
        else:
            # Unselected smooth ring using the same masking technique
            self.canvas.create_oval(
                2,
                2,
                18,
                18,
                fill=self.LIGHT_DARK_BG,
                outline=self.LIGHT_DARK_BG,
            )
            self.canvas.create_oval(
                4, 4, 16, 16, fill=self.DARK_BG, outline=self.DARK_BG
            )


def on_theme_change():
    print(f"Selected Theme: {selected_theme.get()}")


# Initialize the main window
root = tk.Tk()
root.title("Dark Theme Radio Buttons")
root.geometry("300x250")

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
    radio_btn.pack(anchor="w", padx=40, pady=6)

# Start the application loop
root.mainloop()

