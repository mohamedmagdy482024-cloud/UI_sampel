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

            item_frame = tk.Frame(self, bg=self.DARK_BG)
            # Reduced vertical spacing (pady) between rows to 1 pixel for maximum compression
            item_frame.grid(row=grid_row, column=grid_col, sticky="nw", padx=10, pady=1)

            dot = StatusDot(item_frame, row_data["status"], self.DARK_BG)
            dot.pack(side="left", anchor="w", pady=0)

            # Internal padding tightened to 2 pixels as requested
            lbl_status = tk.Label(
                item_frame,
                text=row_data["status_text"],
                font=("Arial", 11),
                bg=self.DARK_BG,
                fg=self.TEXT_COLOR,
            )
            lbl_status.pack(side="left", padx=2)

            lbl_name = tk.Label(
                item_frame,
                text=row_data["name"],
                font=("Arial", 11),
                bg=self.DARK_BG,
                fg=self.TEXT_COLOR,
                anchor="w",
            )
            lbl_name.pack(side="left", padx=2)


# Initialize the main window
root = tk.Tk()
root.title("Dark Theme Data Grid")
# Tightened geometry box to match the ultra-compact grid layout
root.geometry("420x75")
root.configure(bg="#1e222b")

table = ModernGridTable(root)
table.pack(fill="both", expand=True, padx=8, pady=6)

root.mainloop()

