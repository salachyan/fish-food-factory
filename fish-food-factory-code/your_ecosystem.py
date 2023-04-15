from tkinter import *
from PIL import ImageTk, Image
import itertools

root=Tk()
<<<<<<< HEAD
# py -3 -m pip install Pillow
#git add . 
#git commit -m ""
image = Image.open('fish-food-factory-code/background.png')
=======

image = Image.open('background.png')
>>>>>>> bfec807c0d8c680f95b3b2a5278e2d3ebd0e7a17
# The (450, 350) is (height, width)
image = image.resize((400, 400), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)


# Slightly modified, this works for me
my_lbl = Label(image=my_img)
my_lbl.pack()
#
root.mainloop()
