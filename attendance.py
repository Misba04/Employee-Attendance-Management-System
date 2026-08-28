import cv2
import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"

# Create attendance file if it doesn't exist
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee ID", "Name", "Date", "Time", "Status"])

# Load face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load employee mapping
employee_mapping = {}

with open("employee_mapping.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            employee_mapping[int(parts[0])] = parts[1]

# Load employee names
employee_names = {}

with open("employees.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            employee_names[parts[0]] = parts[1]

# Load face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera could not be opened.")
    exit()

marked_today = set()

if os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == datetime.now().strftime("%Y-%m-%d"):
                marked_today.add(f'{row["Employee ID"]}_{row["Date"]}')

print("Attendance system started.")
print("Look at the camera.")
print("Press Q to stop.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Could not access camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        employee_id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 70 and employee_id in employee_mapping:

            employee_code = employee_mapping[employee_id]
            name = employee_names.get(employee_code, "Unknown")

            today = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            key = f"{employee_code}_{today}"

            if key not in marked_today:

                with open(ATTENDANCE_FILE, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        employee_code,
                        name,
                        today,
                        current_time,
                        "Present"
                    ])

                marked_today.add(key)

                print(f"Attendance marked: {employee_code} - {name}")

            text = f"{employee_code} | {name} | Present"

        else:
            text = "Unknown"

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Employee Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Attendance system stopped.")