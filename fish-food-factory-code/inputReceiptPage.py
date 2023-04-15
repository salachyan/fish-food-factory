# # import tkinter as tk
#
# from tkinter import *
# class TestMainApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Receipt List")
#         self.minsize(width=300, height=500)
#         self.testFrame1 = Frame()
#         self.testFrame1 = LabelFrame(self, text = "Input Receipt Here", padx = 20, pady = 20)
#         self.testFrame1.pack(pady=20, padx=10)
#         self.testFrame2 = Frame()
#         self.testFrame3 = Frame()
#         self.testFrame4 = Frame()
#
#
#         lst_of_foods = ["avocado", "cucumber", "onion", "lettuce", "cilantro","rice"]
#         endlist = []
#
#         def CompleteList():
#             newWindow = Tk()
#             self.destroy()
#             newWindow.title("Perishables List")
#             newWindow.minsize(width=300, height=500)
#             newWindow.testFrame1 = LabelFrame(newWindow, text="List of Extracted Groceries", padx=20, pady=20)
#             newWindow.testFrame1.pack(pady=20, padx=10)
#             final = []
#             final_list_of_food = ["avocado", "cucumber", "onion", "lettuce", "cilantro"]
#             for index, item in enumerate(final_list_of_food):
#                 final.append(Label(newWindow.testFrame1, text=item,
#                                            width=20,
#                                            font=('Comic Sans MS', 17),
#                                            anchor="w"))
#                 final[index].pack()
#
#         def listFoods(testFrame,lst_of_foods):
#             for index, item in enumerate(lst_of_foods):
#                 endlist.append(Checkbutton(testFrame,text=item,
#                                     width = 20,
#                                     font =('Comic Sans MS', 17),
#                                     anchor="w"))
#                 endlist[index].pack()
#
#         def buttons(testFrame):
#             var1 = IntVar()
#             frame2 = Frame(self.testFrame1)
#             Button(testFrame, text='Retake photo?').pack()
#             Button(testFrame, text='All set!').pack()
#             # need to make this all set button lead to the next page
#
#             # for i in lst_cbox:
#             #     i.select()
#         listFoods(self.testFrame1,lst_of_foods)
#         buttons(self.testFrame1)
#
#
#         self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')
#
#
#
#
# #DISPLAY THE WINDOW
# TestMainApplication().mainloop()


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
