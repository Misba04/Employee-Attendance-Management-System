# Employee Attendance Management System

## 📌 Project Overview

The Employee Attendance Management System is a Python-based application that uses face recognition to automatically record employee attendance.

The system provides a simple graphical interface for employee registration, face-based attendance, attendance viewing, searching, and attendance summary generation.

## ✨ Features

- Employee registration using face images
- Face detection using OpenCV
- Face recognition using LBPH
- Automatic attendance recording
- Duplicate attendance prevention
- View attendance records
- Search attendance by Employee ID
- Attendance summary
- Simple Tkinter graphical interface
- CSV-based attendance storage

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Tkinter
- CSV
- Haar Cascade
- LBPH Face Recognizer

## 📂 Project Structure

```text
Employee_Attendance_System/
│
├── dataset/
├── main.py
├── register_employee.py
├── capture_faces.py
├── train_model.py
├── recognize_face.py
├── attendance.py
├── view_attendance.py
├── attendance_summary.py
├── employees.txt
├── employee_mapping.txt
├── trainer.yml
├── haarcascade_frontalface_default.xml
└── requirements.txt
