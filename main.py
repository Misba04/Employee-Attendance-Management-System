import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def start_attendance():
    subprocess.Popen(
        [sys.executable, "attendance.py"],
        cwd=PROJECT_DIR
    )


def register_employee():
    subprocess.Popen(
        [sys.executable, "register_employee.py"],
        cwd=PROJECT_DIR
    )


def view_attendance():
    subprocess.Popen(
        [sys.executable, "view_attendance.py"],
        cwd=PROJECT_DIR
    )

def attendance_summary():
    subprocess.Popen(
        [sys.executable, "attendance_summary.py"],
        cwd=PROJECT_DIR
    )


def exit_application():
    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        window.destroy()


window = tk.Tk()
window.configure(bg="lightgray")
window.title("Employee Attendance System")
window.geometry("650x650")
window.resizable(False, False)


# Main heading
title = tk.Label(
    window,
    bg="lightgray",
    text="Employee Attendance System",
    font=("Arial", 24, "bold")
)
title.pack(pady=40)


# Subtitle
subtitle = tk.Label(
    window,
    bg="lightgray",
    text="Face Recognition Based Attendance",
    font=("Arial", 13)
)
subtitle.pack(pady=5)


# Register Employee button
register_button = tk.Button(
    window,
    text="Register Employee",
    font=("Arial", 14, "bold"),
    width=28,
    height=2,
    command=register_employee
)
register_button.pack(pady=15)


# Start Attendance button
start_button = tk.Button(
    window,
    text="Start Attendance",
    font=("Arial", 14, "bold"),
    width=28,
    height=2,
    command=start_attendance
)
start_button.pack(pady=15)


# View Attendance button
view_button = tk.Button(
    window,
    text="View Attendance",
    font=("Arial", 14, "bold"),
    width=28,
    height=2,
    command=view_attendance
)
view_button.pack(pady=15)


summary_button = tk.Button(
    window,
    text="Attendance Summary",
    font=("Arial", 14, "bold"),
    width=28,
    height=2,
    command=attendance_summary
)
summary_button.pack(pady=15)


# Exit button
exit_button = tk.Button(
    window,
    text="Exit",
    font=("Arial", 14, "bold"),
    width=28,
    height=2,
    command=exit_application
)
exit_button.pack(pady=15)


# Footer
footer = tk.Label(
    window,
    bg="lightgray",
    text="Employee Attendance Management System",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=20)


window.mainloop()