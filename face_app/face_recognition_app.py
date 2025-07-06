import cv2
import face_recognition
import os
import numpy as np

# Load known faces
known_face_encodings = []
known_face_names = []

known_dir = "known_faces"
for filename in os.listdir(known_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = face_recognition.load_image_file(os.path.join(known_dir, filename))
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])

# Load test image
test_image = face_recognition.load_image_file("test_images/group.jpg")
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to BGR for OpenCV
test_image_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    if matches:
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

    cv2.rectangle(test_image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(test_image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Show result
cv2.imshow("Face Recognition", test_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()