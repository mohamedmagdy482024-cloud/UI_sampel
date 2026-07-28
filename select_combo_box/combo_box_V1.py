import tkinter as tk
from tkinter import ttk


def on_select(event):
    selected_value = combo_box.get()
    label_status.config(text=f"You selected: {selected_value}")


root = tk.Tk()
root.title("Dark Theme Combo Box")
root.geometry("350x200")

DARK_BG = "#1e222b"
LIGHT_DARK_BG = "#2d3139"
TEXT_COLOR = "#ffffff"

root.config(bg=DARK_BG)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground=DARK_BG,
    background=LIGHT_DARK_BG,
    foreground=TEXT_COLOR,
    bordercolor=LIGHT_DARK_BG,
    arrowcolor=TEXT_COLOR,
    padding=0,
    arrowsize=14
)

style.layout("TCombobox", [
    ('Combobox.field', {
        'side': 'top', 'sticky': 'nswe', 'children': [
            ('Combobox.downarrow', {'side': 'right', 'sticky': 'ns'}),
            ('Combobox.padding', {'side': 'left', 'sticky': 'nswe', 'children': [
                ('Combobox.textarea', {'sticky': 'nswe'})
            ]})
        ]
    })
])

style.map(
    "TCombobox",
    fieldbackground=[("readonly", DARK_BG)],
    foreground=[("readonly", TEXT_COLOR)],
    bordercolor=[("focus", LIGHT_DARK_BG), ("active", LIGHT_DARK_BG)]
)

root.option_add("*TCombobox*Listbox.background", DARK_BG)
root.option_add("*TCombobox*Listbox.foreground", TEXT_COLOR)
root.option_add("*TCombobox*Listbox.selectBackground", LIGHT_DARK_BG)
root.option_add("*TCombobox*Listbox.selectForeground", TEXT_COLOR)

options = ["Python", "JavaScript", "C++", "Java", "Go"]
tight_width = max(len(option) for option in options) 

combo_box = ttk.Combobox(root, values=options, state="readonly", width=tight_width)
combo_box.pack(pady=30)
combo_box.current(0)
combo_box.bind("<<ComboboxSelected>>", on_select)

label_status = tk.Label(
    root,
    text=f"You selected: {combo_box.get()}",
    font=("Arial", 11),
    bg=DARK_BG,
    fg=TEXT_COLOR,
)
label_status.pack(pady=20)

root.mainloop()

