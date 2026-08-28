import tkinter as tk
from tkinter import ttk
import csv
import os

ATTENDANCE_FILE = "attendance.csv"


def load_attendance():
    # Clear existing rows
    for item in table.get_children():
        table.delete(item)

    if not os.path.exists(ATTENDANCE_FILE):
        return

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            table.insert(
                "",
                "end",
                values=(
                    row["Employee ID"],
                    row["Name"],
                    row["Date"],
                    row["Time"],
                    row["Status"]
                )
            )


def search_employee():
    search_id = search_entry.get().strip().upper()

    # Clear table
    for item in table.get_children():
        table.delete(item)

    if not os.path.exists(ATTENDANCE_FILE):
        return

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Employee ID"].upper() == search_id:
                table.insert(
                    "",
                    "end",
                    values=(
                        row["Employee ID"],
                        row["Name"],
                        row["Date"],
                        row["Time"],
                        row["Status"]
                    )
                )


def show_all():
    search_entry.delete(0, tk.END)
    load_attendance()


window = tk.Tk()
window.title("Attendance Records")
window.geometry("800x550")
window.resizable(False, False)


title = tk.Label(
    window,
    text="Employee Attendance Records",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)


# Search section
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

search_label = tk.Label(
    search_frame,
    text="Employee ID:",
    font=("Arial", 12, "bold")
)
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    width=20
)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 11, "bold"),
    command=search_employee
)
search_button.pack(side=tk.LEFT, padx=5)

show_all_button = tk.Button(
    search_frame,
    text="Show All",
    font=("Arial", 11, "bold"),
    command=show_all
)
show_all_button.pack(side=tk.LEFT, padx=5)


# Attendance table
columns = ("Employee ID", "Name", "Date", "Time", "Status")

table = ttk.Treeview(
    window,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=140)

table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# Refresh button
refresh_button = tk.Button(
    window,
    text="Refresh Attendance",
    font=("Arial", 12, "bold"),
    command=load_attendance
)
refresh_button.pack(pady=10)


load_attendance()

window.mainloop()