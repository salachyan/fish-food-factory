from tkinter import *
from PIL import ImageTk, Image
import itertools

root=Tk()

image = Image.open('background.png')
# The (450, 350) is (height, width)
image = image.resize((400, 400), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)


# Slightly modified, this works for me
my_lbl = Label(image=my_img)
my_lbl.pack()
#
root.mainloop()
