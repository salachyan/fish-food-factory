# import tkinter as tk

from tkinter import *
class TestMainApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt List")
        self.minsize(width=300, height=500)
        self.testFrame1 = Frame()
        self.testFrame1 = LabelFrame(self, text = "List of Extracted Groceries", padx = 20, pady = 20)
        self.testFrame1.pack(pady=20, padx=10)
        self.testFrame2 = Frame()
        self.testFrame3 = Frame()
        self.testFrame4 = Frame()
        def listFoods(testFrame):
            lst_of_foods = ["avocado","strawberries","grapes"]
            lst_cbox = []
            for i in range(0,len(lst_of_foods)):
                c1 = Checkbutton(testFrame,text=lst_of_foods[i],
                                    width = 20,
                                    font =('Comic Sans MS', 17)
                                    ,onvalue = 1, offvalue = 0,
                                    anchor="w").pack()

            # for i in lst_cbox:
            #     i.select()
        listFoods(self.testFrame1)

        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')
        self.testFrame2.grid(row=3, column=0, rowspan=3, columnspan=3, sticky='nsew')
        self.testFrame3.grid(row=0, column=3, rowspan=2, columnspan=3, sticky='nsew')
        self.testFrame4.grid(row=2, column=3, rowspan=4, columnspan=3, sticky='nsew')


lst_of_foods = [1,2,3]

#MAKE WINDOW
#
# window = tk.Tk()
# def makeWindow():
#     window.title("FishFoodFactory")
#     window.configure(width = 300, height = 500)
#
#
# def listFoods():
#     frame = tk.Frame()
#
#     for i in range(0,len(lst_of_foods)):
#         vari = tk.IntVar()
#         button = tk.Checkbutton(master = frame,text=lst_of_foods[i],variable=vari).grid(row=i)
#         button.pack()
#
#
#


#DISPLAY THE WINDOW
TestMainApplication().mainloop()