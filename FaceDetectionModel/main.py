import cv2
import tkinter as tk
from tkinter import Button, Entry, Label
from PIL import Image, ImageTk
import numpy as np
import requests

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize GUI
window = tk.Tk()
window.title("Face Recognition System")
window.geometry("800x700")

# Webcam setup
stream = cv2.VideoCapture(0)
if not stream.isOpened():
    print("Cannot open camera")
    exit()

face_database = {}  
capturing_face = False  
new_user_name = ""  

# Extract facial features using histogram
def extract_features(face):
    gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_face], [0], None, [256], [0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

# Save face features in memory
def save_face(face, name):
    global face_database
    features = extract_features(face)
    face_database[name] = features
    print(f"Face features saved for user: {name}")

# Register a new user
def register_user():
    global capturing_face, new_user_name
    new_user_name = name_entry.get().strip()
    if new_user_name:
        capturing_face = True
        status_label.config(text="Look at the camera to capture your face!", fg="blue")
    else:
        status_label.config(text="Please enter a name before registering.", fg="red")

# Authenticate a face
def authenticate_face(face):
    current_features = extract_features(face)
    
    for name, stored_features in face_database.items():
        distance = np.linalg.norm(current_features - stored_features)
        if distance < 0.7:  # Adjust threshold if needed
            print("Authenticate Done")
            send_auth_request()
            return True, name  
    return False, None

# Function to update webcam feed
def update_frame():
    global capturing_face, new_user_name
    ret, frame = stream.read()
    if ret:
        frame = cv2.flip(frame, 1)  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            if capturing_face and new_user_name:
                save_face(face, new_user_name)
                status_label.config(text=f"User '{new_user_name}' registered successfully!", fg="green")
                capturing_face = False
                new_user_name = ""
            else:
                authenticated, name = authenticate_face(face)
                if authenticated:
                    status_label.config(text=f"Authenticated: {name}", fg="green")
                    cv2.putText(frame, f"Authenticated: {name}", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    status_label.config(text="Unauthorized Face Detected!", fg="red")
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(image))
        video_label.config(image=img)
        video_label.image = img

    window.after(10, update_frame)

# Function to close the application
def close_app():
    stream.release()
    cv2.destroyAllWindows()
    window.quit()

def send_auth_request():
    url = 'http://10.10.14.245:8080/'
    boolean_value = True
    response = requests.get(url, json={'bool': boolean_value})
    print("Server Response:", response.text)

# GUI Components
video_label = tk.Label(window)
video_label.pack()

name_label = Label(window, text="Enter your name:")
name_label.pack(pady=5)

name_entry = Entry(window, width=30)
name_entry.pack(pady=5)

register_btn = Button(window, text="Register Face", command=register_user, bg="blue", fg="white")
register_btn.pack(pady=10)

status_label = Label(window, text="", fg="red")
status_label.pack(pady=10)

exit_btn = Button(window, text="Exit", command=close_app, bg="red", fg="white")
exit_btn.pack(pady=20)

update_frame()
window.mainloop()
