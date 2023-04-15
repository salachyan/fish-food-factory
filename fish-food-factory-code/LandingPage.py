import tkinter as tk
from tkinter import font

class LandingPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the landing page
        self.label = tk.Label(self, text="Welcome to the Fish Food Factory!", font=("Comfortaa", 20))
        self.label.pack(pady=20)

        # Create 4 buttons for different pages
        self.button1 = tk.Button(self, text="Page 1", command=self.page1, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="Page 2", command=self.page2, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="Page 3", command=self.page3, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self, text="Page 4", command=self.page4, font=("Comfortaa", 16), bg="#FFE6E6", padx=20, pady=10)
        self.button4.pack(pady=10)

    def page1(self):
        # Replace this with the code for the first page
        print("Page 1")

    def page2(self):
        # Replace this with the code for the second page
        print("Page 2")

    def page3(self):
        # Replace this with the code for the third page
        print("Page 3")

    def page4(self):
        # Replace this with the code for the fourth page
        print("Page 4")


if __name__ == "__main__":
    # Create a root window and set its title
    root = tk.Tk()
    root.title("Fish Food Factory")

    # Set the window size
    root.geometry("400x400")

    # Set the window background color
    root.configure(bg="#FFE6E6")

    # Create a landing page and display it
    landing_page = LandingPage(master=root)
    landing_page.mainloop()
