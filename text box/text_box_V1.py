import tkinter as tk
import re


class ModernTextInput(tk.Entry):

    BASE_BG = "#1e222b"
    HOVER_BG = "#3a3f4d"
    BORDER_COLOR = "#4b5263"
    FOCUS_BORDER = "#2196f3"
    TEXT_COLOR = "#ffffff"

    def __init__(self, parent, placeholder="", default="", on_change=None, **kwargs):
        self.placeholder = placeholder
        self.on_change = on_change
        self._focused = False
        self._hovering = False

        initial_text = default if default else placeholder
        dynamic_width = len(initial_text) + 2 if initial_text else 8

        self.var = tk.StringVar(value=default)
        self.var.trace_add("write", self._on_text_change)

        super().__init__(
            parent,
            textvariable=self.var,
            font=("Arial", 10, "bold"),
            bg=self.BASE_BG,
            fg=self.TEXT_COLOR,
            insertbackground=self.TEXT_COLOR,
            width=dynamic_width,
            justify="left",
            bd=0,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self.BORDER_COLOR,
            highlightcolor=self.FOCUS_BORDER,
            **kwargs,
        )

        if default:
            self.config(fg=self.TEXT_COLOR)
        elif placeholder:
            self.config(fg="#8b919a")
            self.insert(0, placeholder)

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<Enter>", self._on_hover_enter)
        self.bind("<Leave>", self._on_hover_leave)

    def _on_text_change(self, *args):
        content = self.var.get()
        reference = content if content else self.placeholder
        dynamic_width = max(len(reference) + 2, 4)
        self.config(width=dynamic_width)

        if self.on_change:
            self.on_change(content)

    def _apply_style(self):
        if self._focused:
            self.config(bg=self.BASE_BG, highlightbackground=self.FOCUS_BORDER)
        elif self._hovering:
            self.config(bg=self.HOVER_BG, highlightbackground=self.BORDER_COLOR)
        else:
            self.config(bg=self.BASE_BG, highlightbackground=self.BORDER_COLOR)

    def _on_focus_in(self, event):
        self._focused = True
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.TEXT_COLOR)
        self._apply_style()

    def _on_focus_out(self, event):
        self._focused = False
        if not self.get().strip() and self.placeholder:
            self.config(fg="#8b919a")
            self.delete(0, tk.END)
            self.insert(0, self.placeholder)
            dynamic_width = len(self.placeholder) + 2
            self.config(width=dynamic_width)
        self._apply_style()

    def _on_hover_enter(self, event):
        self._hovering = True
        self._apply_style()

    def _on_hover_leave(self, event):
        self._hovering = False
        self._apply_style()

    def get_value(self):
        value = self.get()
        if value == self.placeholder:
            return ""
        return value


class ModernNumberInput(tk.Entry):

    BASE_BG = "#2d3139"
    HOVER_BG = "#3a3f4d"
    BORDER_COLOR = "#2196f3"
    FOCUS_BORDER = "#1e88e5"
    TEXT_COLOR = "#ffffff"

    def __init__(
        self,
        parent,
        default="0",
        min_value=None,
        max_value=None,
        allow_decimal=True,
        on_change=None,
        **kwargs,
    ):
        self.min_value = min_value
        self.max_value = max_value
        self.allow_decimal = allow_decimal
        self.on_change = on_change
        self._focused = False
        self._hovering = False

        dynamic_width = len(str(default)) + 2

        self.var = tk.StringVar(value=str(default))
        self.var.trace_add("write", self._on_text_change)

        super().__init__(
            parent,
            textvariable=self.var,
            font=("Arial", 10, "bold"),
            bg=self.BASE_BG,
            fg=self.TEXT_COLOR,
            insertbackground=self.TEXT_COLOR,
            width=dynamic_width,
            justify="center",
            bd=0,
            relief="flat",
            highlightthickness=2,
            highlightbackground=self.BORDER_COLOR,
            highlightcolor=self.FOCUS_BORDER,
            **kwargs,
        )

        vcmd = (self.register(self._validate_input), "%P")
        self.config(validate="key", validatecommand=vcmd)

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<Enter>", self._on_hover_enter)
        self.bind("<Leave>", self._on_hover_leave)

    def _validate_input(self, value):
        if value in ("", "-", ".", "-."):
            return True

        pattern = r"^-?\d*\.?\d*$" if self.allow_decimal else r"^-?\d*$"
        if not re.match(pattern, value):
            return False

        try:
            numeric = float(value)
        except ValueError:
            return True

        if self.min_value is not None and numeric < self.min_value:
            return False
        if self.max_value is not None and numeric > self.max_value:
            return False

        return True

    def _on_text_change(self, *args):
        content = self.var.get()
        display = content if content else "0"
        dynamic_width = max(len(display) + 2, 4)
        self.config(width=dynamic_width)

        if self.on_change:
            self.on_change(self.get_value())

    def _apply_style(self):
        if self._focused:
            self.config(bg=self.HOVER_BG, highlightbackground=self.FOCUS_BORDER)
        elif self._hovering:
            self.config(bg=self.HOVER_BG, highlightbackground=self.BORDER_COLOR)
        else:
            self.config(bg=self.BASE_BG, highlightbackground=self.BORDER_COLOR)

    def _on_focus_in(self, event):
        self._focused = True
        self._apply_style()

    def _on_focus_out(self, event):
        self._focused = False
        if not self.var.get().strip():
            self.var.set("0")
        self._apply_style()

    def _on_hover_enter(self, event):
        self._hovering = True
        self._apply_style()

    def _on_hover_leave(self, event):
        self._hovering = False
        self._apply_style()

    def get_value(self):
        value = self.var.get().strip()
        if not value or value in ("-", ".", "-."):
            return 0.0 if self.allow_decimal else 0
        return float(value) if self.allow_decimal else int(float(value))


def on_text_change(value):
    print(f"Text input changed: '{value}'")


def on_number_change(value):
    print(f"Number input changed: {value}")


root = tk.Tk()
root.title("Modern Flat Dynamic Text & Number Inputs")
root.configure(bg="#1e222b")

container = tk.Frame(root, bg="#1e222b")
container.pack(padx=20, pady=20)

text_label = tk.Label(
    container,
    text="Text Input (flat outline style)",
    font=("Arial", 10, "bold"),
    bg="#1e222b",
    fg="#ffffff",
)
text_label.grid(row=0, column=0, sticky="w", pady=(0, 8))

text_input = ModernTextInput(
    container,
    placeholder="Enter your email",
    on_change=on_text_change,
)
text_input.grid(row=1, column=0, sticky="w", pady=(0, 20))

number_label = tk.Label(
    container,
    text="Number Input (accent border style)",
    font=("Arial", 10, "bold"),
    bg="#1e222b",
    fg="#ffffff",
)
number_label.grid(row=2, column=0, sticky="w", pady=(0, 8))

number_input = ModernNumberInput(
    container,
    default="100",
    min_value=0,
    max_value=5000,
    allow_decimal=False,
    on_change=on_number_change,
)
number_input.grid(row=3, column=0, sticky="w")

root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()
