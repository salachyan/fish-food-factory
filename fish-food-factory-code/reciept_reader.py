from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x350")

BGImg = PhotoImage(file = "ecosystem.png")
image=  Image.open("ecosystem.png")
resize = image.resize(50,30)

label1 = Label(root,image = resize)
label1.place(x=0,y=0)

# Create a LabelFrame
frame = LabelFrame(root, text="Select the Subjects", padx=20, pady=20)
frame.pack(pady=20, padx=10)

# Create four checkbuttons inside the frame
C1 = Checkbutton(frame, text="Mathematics", width=200, anchor="w").pack()

C2 = Checkbutton(frame, text = "Physics", width=200, anchor="w").pack()

C3 = Checkbutton(frame, text = "Chemistry", width=200, anchor="w").pack()

C4 = Checkbutton(frame, text = "Biology", width=200, anchor="w").pack()

root.mainloop()