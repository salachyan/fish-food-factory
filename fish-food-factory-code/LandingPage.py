import tkinter as tk
import random


class Bubble(tk.Canvas):
    def __init__(self, master=None, size=20, fill="#87CEEB"):
        super().__init__(master, width=size, height=size, highlightthickness=0, bd=0)
        self.create_oval(0, 0, size, size, fill=fill, outline="")
        self.pack()
        self.place(x=random.randint(0, master.winfo_screenwidth()-size),
                   y=random.randint(0, master.winfo_screenheight()-size))


class LandingPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=600, height=600)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_bubbles()

    def create_widgets(self):
        # Set the background color of the landing page
        self.configure(bg="#C6E2FF")

        # Create a label for the landing page
        self.label = tk.Label(self, text="Welcome to the Fish Food Factory!", font=("Comfortaa", 20))
        self.label.pack(pady=30)

        # Create 4 buttons for different pages
        self.button1 = tk.Button(self, text="Page 1", command=self.page1, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="Page 2", command=self.page2, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="Page 3", command=self.page3, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self, text="Page 4", command=self.page4, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button4.pack(pady=10)

    def create_bubbles(self):
        # Create 20 heart widgets and place them randomly around the screen
        for _ in range(20):
            heart = Bubble(master=self, size=20, fill="#87CEEB")

    def page1(self):
        # Replace this with the code for the first page
        print("Enter Receipt")

    def page2(self):
        # Replace this with the code for the second page
        print("My Ecosystem")

    def page3(self):
        # Replace this with the code for the third page
        print("See Current Groceries")

    def page4(self):
        # Replace this with the code for the fourth page
        print("See Food Waste History")


if __name__ == "__main__":
    # Create a root window and set its title
    root = tk.Tk()
    root.title("Fish Food Factory")

    # Set the window size
    root.geometry("600x600")

    # Set the window background color
    root.configure(bg="#FFE6E6")

    # Create a landing page and display it
    landing_page = LandingPage(master=root)
    landing_page.mainloop()
