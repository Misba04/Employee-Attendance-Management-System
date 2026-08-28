import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
employee_ids = []

# Read employee folders
for employee_id in os.listdir(dataset_path):

    employee_folder = os.path.join(dataset_path, employee_id)

    if not os.path.isdir(employee_folder):
        continue

    print(f"Reading images for {employee_id}...")

    for image_name in os.listdir(employee_folder):

        if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(employee_folder, image_name)

        # Images are already cropped face images
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print(f"Could not read: {image_path}")
            continue

        faces.append(image)
        employee_ids.append(employee_id)

print(f"Total face images found: {len(faces)}")

if len(faces) == 0:
    print("No face images found. Please check the dataset.")
    exit()

# Give each employee a numeric label
unique_ids = sorted(set(employee_ids))

id_to_number = {
    employee_id: index
    for index, employee_id in enumerate(unique_ids)
}

numeric_ids = np.array(
    [id_to_number[employee_id] for employee_id in employee_ids],
    dtype=np.int32
)

# Create LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the model
recognizer.train(faces, numeric_ids)

# Save trained model
recognizer.write("trainer.yml")

# Save employee ID mapping
with open("employee_mapping.txt", "w") as file:
    for employee_id, number in id_to_number.items():
        file.write(f"{number},{employee_id}\n")

print("Training completed successfully!")
print("Model saved as trainer.yml")
print("Employee mapping saved as employee_mapping.txt")