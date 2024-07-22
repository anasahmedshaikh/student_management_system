import cv2
import json
from pyzbar.pyzbar import decode
import winsound
import time

    
# Function to scan QR code
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return qr_data
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return None

# Initialize the students JSON object
students = {"students": []}

# Load existing students data if available
try:
    with open("students.json", "r") as file:
        students = json.load(file)
        if "students" not in students:
            students["students"] = []
except FileNotFoundError:
    pass

# Continuously scan for new QR codes
while True:
    print("Scanning for QR code. Press 'q' to quit.")
    qr_data = scan_qr_code()
    if qr_data:
        try:
            student_data = json.loads(qr_data)
            students["students"].append(student_data)
            winsound.Beep(2500, 200)
            # Save the updated students JSON object to a file
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)
            print("Student data added:", student_data)
        except json.JSONDecodeError:
            print("Invalid QR code data.")
    else:
        print("No QR code detected. Exiting.")
        break



