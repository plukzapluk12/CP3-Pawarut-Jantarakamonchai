from tkinter import *
import math

def Leftclick(event):
    bmi = float(textboxWeight.get())/math.pow(float(textboxheight.get())/100, 2)
    if bmi >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif bmi >= 25:
        labelResult.configure(text="อ้วน")
    elif bmi >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmi >= 18.6:
        labelResult.configure(text="ปกติ")
    else:
        labelResult.configure(text="ผอมเกินไป")

Main = Tk()
labelheight = Label(Main,text = "ส่วนสูง (cm.)")
labelheight.grid(row=0,column=0)
textboxheight = Entry(Main)
textboxheight.grid(row=0,column=1)

labelWeight = Label(Main,text = "น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(Main)
textboxWeight.grid(row=1,column=1)

calculatebutton = Button(Main,text="คำนวน")
calculatebutton.bind('<Button-1>',Leftclick)
calculatebutton.grid(row=2,column=0)

labelResult = Label(Main,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

Main.mainloop()