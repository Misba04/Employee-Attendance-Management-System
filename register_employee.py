import cv2
import os

# Get employee details
employee_code = input("Enter Employee ID: ").strip()
employee_name = input("Enter Employee Name: ").strip()

if employee_code == "" or employee_name == "":
    print("Employee ID and Name cannot be empty.")
    exit()

# Create dataset folder
dataset_folder = "dataset"

if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# Create employee folder
employee_folder = os.path.join(dataset_folder, employee_code)

if not os.path.exists(employee_folder):
    os.makedirs(employee_folder)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Could not load Haarcascade file.")
    exit()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera.")
    exit()

count = 0

print("Camera started.")
print("Look at the camera.")
print("Press Q to stop.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Could not read camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        if count >= 30:
            break

        count += 1

        face = gray[y:y+h, x:x+w]

        filename = os.path.join(
            employee_folder,
            f"{employee_code}_{count}.jpg"
        )

        cv2.imwrite(filename, face)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Images: {count}/30",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Employee Registration", frame)

    if count >= 30:
        print("30 images captured.")
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

# Save employee details
with open("employees.txt", "a") as file:
    file.write(f"{employee_code},{employee_name}\n")

print(f"Registration completed for {employee_code} - {employee_name}")
print(f"Total images captured: {count}")