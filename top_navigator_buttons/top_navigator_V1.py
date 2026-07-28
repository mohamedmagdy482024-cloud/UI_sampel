import tkinter as tk


class ModernNavBar(tk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg="#1e222b", **kwargs)

        # Exact premium dark theme colors matched with your design system
        self.DARK_BG = "#1e222b"
        self.HOVER_BG = "#2d3139"
        self.TEXT_COLOR = "#ffffff"
        self.ACCENT_BLUE = "#2196f3"  # Glowing blue for active underline tab

        # Professional names for your dashboard navigator tabs
        self.menu_items = ["Dashboard", "Analytics", "Inventory", "Settings"]
        self.buttons = {}
        self.active_tab = "Dashboard"

        self._build_navbar()

    def _build_navbar(self):
        for item in self.menu_items:
            # Container for each button tab to safely render the bottom active line indicator
            btn_container = tk.Frame(self, bg=self.DARK_BG)
            btn_container.pack(side="left", padx=2)

            # Core navigation text button
            btn = tk.Label(
                btn_container,
                text=item,
                font=("Arial", 11, "bold"),
                bg=self.DARK_BG,
                fg=self.TEXT_COLOR,
                padx=18,
                pady=12,
                cursor="hand2"
            )
            btn.pack(side="top")

            # Flat bottom underline tracking highlight line
            underline = tk.Frame(btn_container, bg=self.DARK_BG, height=3)
            underline.pack(side="top", fill="x")

            # Store references to dynamically toggle active highlight animations
            self.buttons[item] = {"btn": btn, "line": underline}

            # Bind interactive hover and selection click events
            btn.bind("<Enter>", lambda e, item=item: self._on_hover_enter(item))
            btn.bind("<Leave>", lambda e, item=item: self._on_hover_leave(item))
            btn.bind("<Button-1>", lambda e, item=item: self._on_tab_click(item))

        # Render the default selected tab highlight on startup
        self._update_tab_visuals()

    def _on_hover_enter(self, item):
        # Brighten background smoothly on hover
        self.buttons[item]["btn"].config(bg=self.HOVER_BG)

    def _on_hover_leave(self, item):
        # Reset background back to dark theme flat profile when mouse leaves
        self.buttons[item]["btn"].config(bg=self.DARK_BG)

    def _on_tab_click(self, item):
        self.active_tab = item
        self._update_tab_visuals()
        print(f"Navigation triggered: Selected {item} panel")

    def _update_tab_visuals(self):
        # Loop through all elements to light up the active tab and extinguish old ones
        for item, widgets in self.buttons.items():
            if item == self.active_tab:
                widgets["line"].config(bg=self.ACCENT_BLUE)
            else:
                widgets["line"].config(bg=self.DARK_BG)


# Initialize the main window
root = tk.Tk()
root.title("Modern Dark Top Navigator")
root.configure(bg="#1e222b")

# Instantiate and render the elite top navigation bar
navbar = ModernNavBar(root)
navbar.pack(fill="x", side="top")

# Force window sizing engine to shrink and wrap perfectly around content dimensions
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()+100}")

root.mainloop()

