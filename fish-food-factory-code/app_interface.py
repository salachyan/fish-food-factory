# import tkinter as tk


from tkinter import *
class TestMainApplication2(Tk):
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
            newWindow.minsize(width=300, height=500)
            newWindow.testFrame1 = LabelFrame(newWindow, text="List of Extracted Groceries", padx=20, pady=20)
            newWindow.testFrame1.pack(pady=20, padx=10)
            final = []
            final_list_of_food = ["avocado", "cucumber", "onion", "lettuce", "cilantro"]
            for index, item in enumerate(final_list_of_food):
                final.append(Label(newWindow.testFrame1, text=item,
                                           width=20,
                                           font=('Comic Sans MS', 17),
                                           anchor="w"))
                final[index].pack()

        def listFoods(testFrame,lst_of_foods):
            for index, item in enumerate(lst_of_foods):
                endlist.append(Checkbutton(testFrame,text=item,
                                    width = 20,
                                    font =('Comic Sans MS', 17),
                                    anchor="w"))
                endlist[index].pack()

        def buttons(testFrame):
            var1 = IntVar()
            frame2 = Frame(self.testFrame1)
            Button(testFrame, text='Select All', command=select_all).pack()
            Button(testFrame, text='Deselect All', command=deselect_all).pack()
            Label(testFrame,  text='Missing an Item? Add it!').pack()
            Text(testFrame,height = 1,width=15).pack()
            Button(testFrame, text= 'Add Missing Item',command=add_item).pack()
            Button(testFrame,text="Everythings In!", command=CompleteList).pack()
            self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')

            # for i in lst_cbox:
            #     i.select()
        listFoods(self.testFrame1,lst_of_foods)
        buttons(self.testFrame1)


        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')




#DISPLAY THE WINDOW
print("BYE")
TestMainApplication2().mainloop()