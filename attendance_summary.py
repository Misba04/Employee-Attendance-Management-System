import tkinter as tk
from tkinter import ttk
import csv
import os

ATTENDANCE_FILE = "attendance.csv"


def load_summary():
    for item in table.get_children():
        table.delete(item)

    summary = {}

    if not os.path.exists(ATTENDANCE_FILE):
        return

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employee_id = row["Employee ID"]
            name = row["Name"]
            date = row["Date"]

            if employee_id not in summary:
                summary[employee_id] = {
                    "name": name,
                    "dates": set()
                }

            summary[employee_id]["dates"].add(date)

    for employee_id, data in summary.items():
        total_days = len(data["dates"])
        last_date = max(data["dates"])

        table.insert(
            "",
            "end",
            values=(
                employee_id,
                data["name"],
                total_days,
                last_date
            )
        )


window = tk.Tk()
window.title("Attendance Summary")
window.geometry("700x450")

title = tk.Label(
    window,
    text="Attendance Summary",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

columns = (
    "Employee ID",
    "Name",
    "Total Present Days",
    "Last Attendance"
)

table = ttk.Treeview(
    window,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=160)

table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

refresh_button = tk.Button(
    window,
    text="Refresh Summary",
    font=("Arial", 12, "bold"),
    command=load_summary
)

refresh_button.pack(pady=15)

load_summary()

window.mainloop()