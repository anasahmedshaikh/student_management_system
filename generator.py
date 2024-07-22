from qrcode import qrcode
import json

# input data
print("----------Enter Student's Details----------") 
name = input("Enter Student's name: ")
age = int(input("Enter Student's age: "))
_class = input("Enter Student's class: ")

data = {
    "name": name,
    "age": age,
    "class": _class
} 
json_data = json.dumps(data)
qr_img = qrcode.make(json_data)  
# saving the image file  
qr_img.save(f"{name}-qr.jpg") 
print("QR code generated successfully!")
