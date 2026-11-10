import qrcode
from datetime import datetime

students = ["Gayatri", "Rutuja", "Priya"]

attendance = []

name = input("Enter student name: ")

if name in students:
    time = datetime.now().strftime("%H:%M:%S")

    attendance.append(name)

    data = f"Name: {name}\nTime: {time}"

    qr = qrcode.make(data)
    qr.save(name + "_attendance.png")

    print("Attendance QR Generated!")
    print("Student:", name)
    print("Time:", time)
else:
    print("Student not registered!")