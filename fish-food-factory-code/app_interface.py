import tkinter

from PIL import Image, ImageTk
from tkinter import *


class ReceiptReader(Tk):
    def __init__(self):
        super().__init__()
        self.frame = Frame(self,width = 600, height = 400)
        self.frame.pack()
        imag = Image.open("fish-food-factory-code/harrisTeeter.jpg")
        harrisTeet = ImageTk.PhotoImage(imag)
        label = Label(self.frame,image = harrisTeet)
        label.pack()

        Button(self.frame, text='Use This Image', bg="#FFE6E6", command=TestMainApplication().mainloop()).pack()


class TestMainApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt List")
        self.configure(bg="#FFE6E6")
        self.minsize(width=300, height=500)
        self.testFrame1 = Frame()

        self.testFrame1 = LabelFrame(self, text = "List of Extracted Groceries", bg="#FFE6E6",padx = 20, pady = 20)
        self.testFrame1.pack(pady=20, padx=10)
        self.testFrame2 = Frame()
        self.testFrame3 = Frame()
        self.testFrame4 = Frame()


        lst_of_foods = ["avocado", "cucumber", "onion", "lettuce", "cilantro","rice"]
        endlist = []
        def select_all():
            for i in endlist:
                i.select()

        def deselect_all():
            for i in endlist:
                i.deselect()

        def add_item():
            lst_of_foods_new = ["avocado","cucumber","onion", "lettuce", "cilantro","rice"]
            listFoods(self.grocerylist,lst_of_foods_new)

        def CompleteList():
            newWindow = Tk()
            self.destroy()

            newWindow.title("Perishables List")
            newWindow.configure(bg="#FFE6E6")
            newWindow.minsize(width=300, height=500)
            newWindow.testFrame1 = LabelFrame(newWindow, text="List of Extracted Groceries", bg="#FFE6E6", padx=20, pady=20)
            newWindow.testFrame1.pack(pady=20, padx=10)
            final = []
            final_list_of_food = ["avocado", "cucumber", "onion", "lettuce", "cilantro"]
            for index, item in enumerate(final_list_of_food):
                final.append(Label(newWindow.testFrame1, text=item,
                                           width=20,
                                           font=('Comic Sans MS', 17),
                                           anchor="w",bg="#FFE6E6"))
                final[index].pack()
            Button(newWindow.testFrame1, text='Select All',bg="#FFE6E6", command=select_all).pack()

        def listFoods(testFrame,lst_of_foods):
            for index, item in enumerate(lst_of_foods):
                endlist.append(Checkbutton(testFrame,text=item,
                                    width = 20,
                                    font =('Comic Sans MS', 17),bg="#FFE6E6",
                                    anchor="w"))
                endlist[index].pack()

        def buttons(testFrame):
            var1 = IntVar()
            frame2 = Frame(self.testFrame1)
            Button(testFrame, text='Select All',bg="#FFE6E6", command=select_all).pack()
            Button(testFrame, text='Deselect All', bg="#FFE6E6",command=deselect_all).pack()
            Label(testFrame,  text='Missing an Item? Add it!',bg="#FFE6E6").pack()
            Text(testFrame,height = 1,width=15,bg="#FFE6E6").pack()
            Button(testFrame, text= 'Add Missing Item',command=add_item,bg="#FFE6E6").pack()
            Button(testFrame,text="Everythings In!", command=CompleteList,bg="#FFE6E6").pack()
            self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')

            # for i in lst_cbox:
            #     i.select()
        listFoods(self.testFrame1,lst_of_foods)
        buttons(self.testFrame1)


        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')




#DISPLAY THE WINDOW
ReceiptReader().mainloop()