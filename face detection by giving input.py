import cv2
import face_recognition

# Load known face encodings and their names
known_face_encodings = []
known_face_names = []

# Load known face images and encodings
known_faces = {
    "Sundar Pichai": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\th.jpg",
    "Satya Nadella": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\OIP (5).jpg",
    "Bill Gates": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\OIP (4).jpg"
}

# Encode the known face images
for name, file in known_faces.items():
    known_image = face_recognition.load_image_file(file)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    known_face_encodings.append(known_encoding)
    known_face_names.append(name)

# Load the input image where you want to detect and recognize faces
input_image_path = "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\OIP (4).jpg"
input_image = face_recognition.load_image_file(input_image_path)

# Convert the image to RGB (OpenCV uses BGR by default)
rgb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Find all face locations and encodings in the input image
face_locations = face_recognition.face_locations(rgb_image)
face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

# Loop through each face found in the input image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Default to "Unknown" name if no match is found
    name = "Unknown"
    
    # Compare face encoding with all known face encodings
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
    # Find the best match among all known faces
    for i, match in enumerate(matches):
        if match:
            name = known_face_names[i]
            break

    # Draw a bounding box around the face
    cv2.rectangle(rgb_image, (left, top), (right, bottom), (0, 0, 255), 2)
    # Display the name below the bounding box
    cv2.putText(rgb_image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

# Convert the image back to BGR for displaying with OpenCV
bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

# Display the processed image
cv2.imshow("Image", bgr_image)
cv2.waitKey(0)  # Wait for a key press to close the image window
cv2.destroyAllWindows()
