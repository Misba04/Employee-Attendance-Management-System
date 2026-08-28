import cv2
import os

# Ask for employee details
employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")

# Create employee folder inside dataset
employee_folder = os.path.join("dataset", employee_id)

if not os.path.exists(employee_folder):
    os.makedirs(employee_folder)

# Load OpenCV face detector
face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found!")
    exit()

print("Camera started.")
print("Look at the camera...")
print("Press Q to stop.")

count = 0

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        count += 1

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        # Save face image
        filename = os.path.join(
            employee_folder,
            f"{employee_id}_{count}.jpg"
        )

        cv2.imwrite(filename, gray[y:y + h, x:x + w])

        cv2.putText(
            frame,
            f"Images: {count}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Employee Face Capture", frame)

    # Stop after 50 images
    if cv2.waitKey(1) & 0xFF == ord("q") or count >= 50:
        break

camera.release()
cv2.destroyAllWindows()

print(f"Captured {count} face images.")
print(f"Images saved in: {employee_folder}")