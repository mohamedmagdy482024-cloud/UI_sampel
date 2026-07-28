import tkinter as tk


class StatusDot(tk.Canvas):

    def __init__(self, parent, status_type, bg_color, **kwargs):
        super().__init__(
            parent,
            width=14,
            height=14,
            bg=bg_color,
            highlightthickness=0,
            **kwargs,
        )

        colors = {
            "active": "#4caf50",
            "starting": "#2196f3",
            "disabled": "#757575",
        }

        dot_color = colors.get(status_type, "#757575")
        self.create_oval(1, 1, 13, 13, fill=dot_color, outline=dot_color)


class ModernGridTable(tk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg="#1e222b", **kwargs)

        self.DARK_BG = "#1e222b"
        # Changed to a much brighter and clearer gray for visible borders
        self.LIGHT_DARK_BG = "#4b5263"  
        self.TEXT_COLOR = "#ffffff"

        self.table_data = [
            {"status": "disabled", "status_text": "Disabled", "name": "Load balancer 3"},
            {"status": "starting", "status_text": "Starting", "name": "Load balancer 1"},
            {"status": "active", "status_text": "Active", "name": "Load balancer 4"},
            {"status": "active", "status_text": "Active", "name": "Load balancer 2"},
        ]

        self._build_grid_layout()

    def _build_grid_layout(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)

        for index, row_data in enumerate(self.table_data):
            grid_row = index % 2
            grid_col = index // 2

            # Main container with a 1px clear visible outer border layout
            item_frame = tk.Frame(
                self, 
                bg=self.DARK_BG,
                highlightbackground=self.LIGHT_DARK_BG,
                highlightthickness=1
            )
            item_frame.grid(row=grid_row, column=grid_col, sticky="nw", padx=4, pady=4)

            # Left section: Status container (Dot + Text)
            status_container = tk.Frame(item_frame, bg=self.DARK_BG)
            status_container.pack(side="left", padx=(6, 2), pady=4)

            dot = StatusDot(status_container, row_data["status"], self.DARK_BG)
            dot.pack(side="left", anchor="w", pady=0)

            lbl_status = tk.Label(
                status_container,
                text=row_data["status_text"],
                font=("Arial", 11),
                bg=self.DARK_BG,
                fg=self.TEXT_COLOR,
                width=7,
                anchor="w"
            )
            lbl_status.pack(side="left", padx=2)

            # Center section: Brighter vertical border line inside the card box
            vertical_border = tk.Frame(item_frame, bg=self.LIGHT_DARK_BG, width=1)
            vertical_border.pack(side="left", fill="y", padx=4)

            # Right section: Name Text
            lbl_name = tk.Label(
                item_frame,
                text=row_data["name"],
                font=("Arial", 11),
                bg=self.DARK_BG,
                fg=self.TEXT_COLOR,
                anchor="w",
            )
            lbl_name.pack(side="left", padx=(4, 8), pady=4)


# Initialize the main window
root = tk.Tk()
root.title("status indicator")
root.configure(bg="#1e222b")

table = ModernGridTable(root)
table.pack(fill="both", expand=True, padx=10, pady=10)

# FORCE WINDOW SIZE TO FIT CONTENT PERFECTLY
# This updates the idle tasks and automatically shrinks/wraps the window to the exact dimensions needed
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()

