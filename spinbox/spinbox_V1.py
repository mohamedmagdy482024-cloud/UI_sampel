import tkinter as tk


def update_width(*args):
    current_value = str(text_variable.get())

    # Add 4 extra padding units to accommodate the control arrows
    dynamic_width = len(current_value) + 1
    spin_box.config(width=dynamic_width)


# Initialize the main window
root = tk.Tk()
root.title("Dark Theme Spinbox")
root.geometry("300x150")

# Matching the exact Combobox background colors
DARK_BG = "#1e222b"
LIGHT_DARK_BG = "#2d3139"
TEXT_COLOR = "#ffffff"

# Apply dark theme background to the main window
root.configure(bg=DARK_BG)

# Declare the tracking variable
text_variable = tk.DoubleVar()

# Create the dark theme Spinbox with matching theme colors
spin_box = tk.Spinbox(
    root,
    from_=1.0,
    to=100000.0,
    increment=1.0,
    textvariable=text_variable,
    font=("Arial", 12, "bold"),
    justify="center",
    # Color configuration matched with Combobox
    bg=DARK_BG,
    fg=TEXT_COLOR,
    buttonbackground=LIGHT_DARK_BG,
    activebackground=LIGHT_DARK_BG,
    insertbackground=TEXT_COLOR,
    # Border styling
    bd=1,
    relief="flat",
)

# Trigger width updates whenever the variable value changes
text_variable.trace_add("write", update_width)

# Set initial value to trigger the layout width calculation
text_variable.set(1.0)

# Render widget with padding
spin_box.pack(pady=50)

# Start the application loop
root.mainloop()

