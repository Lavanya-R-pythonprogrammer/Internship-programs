import cv2
import face_recognition

# Load known face encodings and their names
known_face_encodings = []
known_face_names = []

# Load known face images and encodings
known_faces = {
    "Sundar Pichai": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\th.jpg",
    "Satya Nadella": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\OIP (5).jpg",
    "Bill Gates": "C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\OIP (4).jpg",
    "Lavanya":"C:\\Users\\Lavanya R\\OneDrive\\Pictures\\Saved Pictures\\lr.png"
}

for name, file in known_faces.items():
    known_image = face_recognition.load_image_file(file)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    known_face_encodings.append(known_encoding)
    known_face_names.append(name)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Default to "Unknown" name
        name = "Unknown"
        
        # Compare face encoding with all known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
        # Find the best match among all known faces
        for i, match in enumerate(matches):
            if match:
                name = known_face_names[i]
                break

        # Draw bounding box and display name on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the processed frame
    cv2.imshow("Video", frame)
    
    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()

