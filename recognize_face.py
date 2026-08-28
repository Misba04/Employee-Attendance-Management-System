import cv2

# Load face detector
face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Load trained face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Read employee ID mapping
employee_mapping = {}

with open("employee_mapping.txt", "r") as file:
    for line in file:
        number, employee_id = line.strip().split(",")
        employee_mapping[int(number)] = employee_id

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found!")
    exit()

print("Camera started.")
print("Look at the camera.")
print("Press Q to stop.")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not read camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        employee_number, confidence = recognizer.predict(
            gray[y:y + h, x:x + w]
        )

        employee_id = employee_mapping.get(
            employee_number,
            "Unknown"
        )

        # LBPH confidence is a distance:
        # lower value generally means a better match
        if confidence < 70:
            label = f"{employee_id} | Confidence: {confidence:.1f}"
        else:
            label = "Unknown"

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Employee Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Face recognition stopped.")