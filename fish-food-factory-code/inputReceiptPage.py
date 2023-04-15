

from tkinter import *
from PIL import ImageTk, Image
import app_interface


class HarrisTeeter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt List")
        self.minsize(width=300, height=500)

        # Create a label frame for the image
        self.image_frame = LabelFrame(self, text="Receipt Image", padx=20, pady=20)
        self.image_frame.pack(pady=20, padx=10)

        # Load the image using PIL
        image = Image.open("harrisTeeter.jpg")
        image = image.resize((300, 400), Image.ANTIALIAS)  # Resize the image to fit the label frame
        self.photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.image_label = Label(self.image_frame, image=self.photo)
        self.image_label.pack()

        # Create a button to go to the next page
        self.next_button = Button(self, text="All Good!", command=self.next_page)
        self.next_button.pack(pady=20)

        self.retake_button = Button(self, text="Retake Photo?", command=self.next_page)
        self.retake_button.pack(pady=20)


    def next_page(self):
        # Add your code here to go to the next page
        print("Hello")
        #app_interface.mainloop()


# DISPLAY THE WINDOW
HarrisTeeter().mainloop()
