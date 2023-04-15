from tkinter import *
import random
#import matplotlib.pyplot as plt
#import numpy as np
import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot as plt


class CompleteList(Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt List")
        self.configure(bg="#FFE6E6")
        self.testFrame1 = Frame()

        self.testFrame1 = LabelFrame(self, text="List of Extracted Groceries", bg="#FFE6E6", padx=20, pady=20)
        self.testFrame1.pack(pady=20, padx=10)
        self.testFrame2 = Frame()
        self.testFrame3 = Frame()
        self.testFrame4 = Frame()
        final = []
        final_list_of_food = ["avocado", "cucumber", "onion", "lettuce", "cilantro"]

        def delete():
            self.destroy()
            LandingPage().mainloop()


        def finallist():
            for index, item in enumerate(final_list_of_food):
                final.append(Label(self, text=item,
                                           width=20,
                                           font=('Comic Sans MS', 17),
                                           anchor="w",bg="#FFE6E6"))
                final[index].pack()

        finallist()
        Button(self, text='Back to Home',bg="#FFE6E6",command = delete).pack()

        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')


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


        def listFoods(testFrame,lst_of_foods):
            for index, item in enumerate(lst_of_foods):
                endlist.append(Checkbutton(testFrame,text=item,
                                    width = 20,
                                    font =('Comic Sans MS', 17),bg="#FFE6E6",
                                    anchor="w"))
                endlist[index].pack()
        def runList():
            self.destroy()
            CompleteList().mainloop()

        def buttons(testFrame):
            var1 = IntVar()
            frame2 = Frame(self.testFrame1)
            Button(testFrame, text='Select All',bg="#FFE6E6", command=select_all).pack()
            Button(testFrame, text='Deselect All', bg="#FFE6E6",command=deselect_all).pack()
            Label(testFrame,  text='Missing an Item? Add it!',bg="#FFE6E6").pack()
            Text(testFrame,height = 1,width=15,bg="#FFE6E6").pack()
            Button(testFrame, text= 'Add Missing Item',command=add_item,bg="#FFE6E6").pack()
            Button(testFrame,text="Everythings In!", command=runList,bg="#FFE6E6").pack()
            self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')

            # for i in lst_cbox:
            #     i.select()
        listFoods(self.testFrame1,lst_of_foods)
        buttons(self.testFrame1)


        self.testFrame1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')


class Bubble(Canvas):
    def __init__(self, master=None, size=50):
        super().__init__(master, width=size, height=size, highlightthickness=0, bd=0)
        image = Image.open('bubble.png').resize((size, size))
        self.photo = ImageTk.PhotoImage(image)
        self.create_image(0, 0, image=self.photo, anchor=NW)
        self.pack()
        self.place(x=random.randint(0, master.winfo_screenwidth()-2*size),
                   y=random.randint(0, master.winfo_screenheight()-2*size))


class LandingPage(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_bubbles()

    def create_widgets(self):
        # Create a canvas for the background image
        self.canvas = Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        # Load and display the background image
        self.bg_image = Image.open('landingBackground.png')
        width, height = self.bg_image.size
        bg = self.bg_image.resize((width // 3, height // 3))
        self.bg_image = ImageTk.PhotoImage(bg)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)
        # Set the background color of the landing page
        #self.configure(bg="#C6E2FF")

        # Create a label for the landing page
        self.label = Label(self, text="Welcome to the Fish Food Factory!", font=("Comic Sans MS", 20))
        self.label.pack(pady=30)

        # Create 4 buttons for different pages
        self.button1 = Button(self, text="Enter Receipt", command=self.page1, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button1.pack(pady=10)

        self.button2 = Button(self, text="My Ecosystem", command=self.page2, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button2.pack(pady=10)

        self.button3 = Button(self, text="See Current Groceries", command=self.page3, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button3.pack(pady=10)

        self.button4 = Button(self, text="See Food Waste History", command=self.page4, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button4.pack(pady=10)

        self.button5 = Button(self, text="Your Awards", command=self.page5, font=("Comic Sans MS", 16),
                          bg="#FFE6E6", padx=20, pady=10)
        self.button5.pack(pady=10)

    def create_bubbles(self):
        # Create 20 heart widgets and place them randomly around the screen
        for _ in range(20):
            bubble = Bubble(master=self, size=20)

    def page1(self):
        # Replace this with the code for the first page
        self.destroy()
        TestMainApplication().mainloop()

    def page2(self):
        # Replace this with the code for the second page
        self.destroy()
        root = Tk()

        image = Image.open('ecosystemwithFish.png')
        # The (450, 350) is (height, width)
        image = image.resize((400, 400), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)

        # Slightly modified, this works for me
        my_lbl = Label(image=my_img)
        my_lbl.pack()
        #
        root.mainloop()

    def page3(self):
        # Replace this with the code for the third page
        # Current_Grocier
        print("Enter Receipt")

    def page4(self):
        # Generate fake data for food wasted per week
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        food_waste = np.random.randint(1, 10, size=len(weeks))

        # Create a bar chart of the data
        fig, ax = plt.subplots()
        ax.bar(weeks, food_waste)

        # Set chart title and axis labels
        ax.set_title('Amount of Food Wasted per Week (lbs)')
        ax.set_xlabel('Weeks')
        ax.set_ylabel('Amount of Food Wasted')

        # Display the chart
        plt.show()

    def page5(self):
        # Replace this with the code for the third page
        # Current_Grocier
        self.destroy()
        root = Tk()

        image = Image.open('awardsWithShell.png')
        # The (450, 350) is (height, width)
        image = image.resize((400, 400), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)

        # Slightly modified, this works for me
        my_lbl = Label(image=my_img)
        my_lbl.pack()
        #
        root.mainloop()

if __name__ == "__main__":
    # Create a root window and set its title
    root = Tk()
    root.title("Fish Food Factory")

    # Set the window size
    # root.geometry("600x600")

    # Set the window background color
    # root.configure(bg="#FFE6E6")

    # Create a landing page and display it
    landing_page = LandingPage(master=root)
    landing_page.mainloop()