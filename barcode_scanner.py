import cv2
import json
from pyzbar.pyzbar import decode
import winsound

def BarcodeReader(): 
      
    # read the image in numpy array using cv2 
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
# Decode the barcode image 
        detectedBarcode = decode(frame)
        for barcode in detectedBarcode:
            bar_data = barcode.data.decode('utf-8')
            if barcode.data!="":
                print(barcode.data) 
                print(barcode.type)
                cap.release()
                cv2.destroyAllWindows()
                return bar_data
        cv2.imshow("BAR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return None
    
students = {"students": []}

# Load existing students data if available
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    pass

# Continuously scan for new QR codes
while True:
    print("Scanning for QR code. Press 'q' to quit.")
    br_data = BarcodeReader()
    if br_data:
        try:
            student_data = json.loads(str(br_data))
            students["students"].append(student_data)
            winsound.Beep(2500, 200)
            # Save the updated students JSON object to a file
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)
            print("Student data added:", student_data)
        except json.JSONDecodeError:
            print("Invalid bar code data.")
    else:
        print("No bar code detected. Exiting.")
        break