import cv2
import webbrowser
from pyzbar.pyzbar import decode
import numpy
import qrcode
import random
from tkinter import *
import winsound
from PIL import ImageTk, Image
cd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

stu = {}

def add():
    add = Tk()
    add.geometry('500x500')
    add.config(bg="white")
    name = Label(add, text="Student Name:", bg="white", font="cursive 15")
    name.place(x=100, y=100, height=50, width=150)
    nameg = Entry(add, bd=0, font="cursive 15", bg="light grey")
    nameg.place(x=250, y=110, height=30, width=150)

    mail = Label(add, text="VIT Mail ID:", bg="white", font="cursive 15")
    mail.place(x=100, y=170, height=50, width=150)
    mailg = Entry(add, bd=0, font="cursive 15", bg="light grey")
    mailg.place(x=250, y=180, height=30, width=150)

    def add_val():
        n = nameg.get()
        m = mailg.get()
        file = open("students.txt", "a")
        file.write(n+":"+m+";")
        file.close()
        

    submit = Button(add, text="Add", command=add_val, bd=0, font="cursive 15", bg="#302f7d", fg="white")
    submit.place(x=240, y=270, height=40, width=70)
    add.mainloop()

root = Tk()
logo_lbl = Label(root, bg="#302f7d", text="Vellore Institute of Technology", font="cursive 40", fg="white").place(x=0, y=0, height=100, width=1300)
add_stu = Button(root, bg="#302f7d", text="+", font="cursive 50", fg="white", bd=0, command=add).place(x=1100, y=600, height=70, width=70)
logo_img = ImageTk.PhotoImage(Image.open(r"C:\Users\vkpvk\AppData\Local\Programs\Python\Python39\vit.png"))
logo = Label(root, image=logo_img).place(x=150, y=0, height=100, width=100)
root.mainloop()

def extract_stu():
    file = open("students.txt", "r")
    sts = file.read()
    sts = sts.split(";")
    val = []
    sts.pop()
    for i in sts:
        val.append(i.split(":"))
    print(val)
    file.close()
    

def gen_code():
    for j in stu:
        var=""
        for i in range(10):
            var = var + cd[random.randint(0, 69)]
        file = open(r"C:\Users\vkpvk\OneDrive\Desktop\database.txt", 'a')
        file.write(j+":"+var+":"+stu[j]+";")
        file.close()

def send_msg():
    file = open(r"C:\Users\vkpvk\OneDrive\Desktop\database.txt", 'r')
    val = file.read()
    acc = []
    vals = val.split(";")
    vals.pop()
    for i in vals:
        acc.append(i.split(":"))
    for i in acc:
        img = qrcode.make(i[1])
        img.save(r"C:\Users\vkpvk\OneDrive\Desktop\New folder\v"+str(i[1])+".png")
        pywhatkit.sendwhats_image(i[2], r"C:\Users\vkpvk\OneDrive\Desktop\New folder\v"+str(i[1])+".png", "Vit attendance", 20)

def scan():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    arr = []
    while True:
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode()
            if myData in arr:
               pass
            else:
                arr.append(myData)
                print(myData)
                winsound.Beep(6000, 11)
                

        cv2.imshow('result', img)
        cv2.waitKey(1)



    
extract_stu()


