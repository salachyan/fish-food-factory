import tkinter as tk
import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk


class Bubble(tk.Canvas):
    def __init__(self, master=None, size=50):
        super().__init__(master, width=size, height=size, highlightthickness=0, bd=0)
        image = Image.open("bubble.png").resize((size, size))
        self.photo = ImageTk.PhotoImage(image)
        self.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.pack()
        self.place(x=random.randint(0, master.winfo_screenwidth()-2*size),
                   y=random.randint(0, master.winfo_screenheight()-2*size))


class LandingPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_bubbles()

    def create_widgets(self):
        # Create a canvas for the background image
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        # Load and display the background image
        self.bg_image = Image.open("landingBackground.png")
        width, height = self.bg_image.size
        bg = self.bg_image.resize((width // 5, height // 5))
        self.bg_image = ImageTk.PhotoImage(bg)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=tk.NW)
        # Set the background color of the landing page
        #self.configure(bg="#C6E2FF")

        # Create a label for the landing page
        self.label = tk.Label(self, text="Welcome to the Fish Food Factory!", font=("Comic Sans MS", 20))
        self.label.pack(pady=30)

        # Create 4 buttons for different pages
        self.button1 = tk.Button(self, text="Enter Receipt", command=self.page1, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="My Ecosystem", command=self.page2, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="See Current Groceries", command=self.page3, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self, text="See Food Waste History", command=self.page4, font=("Comic Sans MS", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button4.pack(pady=10)

    def create_bubbles(self):
        # Create 20 heart widgets and place them randomly around the screen
        for _ in range(20):
            bubble = Bubble(master=self, size=20)

    def page1(self):
        # Replace this with the code for the first page
        print("Enter Receipt")

    def page2(self):
        # Replace this with the code for the second page
        print("Enter Receipt")

    def page3(self):
        # Replace this with the code for the third page
        print("Enter Receipt")

    def page4(self):
        # Generate fake data for food wasted per week
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        food_waste = np.random.randint(1, 10, size=len(weeks))

        # Create a bar chart of the data

        fig, ax = plt.subplots()
        plt.plot(weeks, food_waste, color='#60FFFF', linestyle='dashed', linewidth = 1,
         marker='o', markerfacecolor='#FF94F7', markersize=12)

        # Set chart title and axis labels
        ax.set_title('Amount of Food Wasted per Week in lbs')
        ax.set_xlabel('Weeks')
        ax.set_ylabel('Amount of Food Wasted (lbs)')

        # Display the chart
        plt.show()


if __name__ == "__main__":
    # Create a root window and set its title
    root = tk.Tk()
    root.title("Fish Food Factory")

    # Set the window size
    # root.geometry("600x600")

    # Set the window background color
    # root.configure(bg="#FFE6E6")

    # Create a landing page and display it
    landing_page = LandingPage(master=root)
    landing_page.mainloop()
