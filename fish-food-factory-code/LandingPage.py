import tkinter as tk


class LandingPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the landing page
        self.label = tk.Label(self, text="Welcome to My Website!")
        self.label.pack(pady=20)

        # Create 4 buttons for different pages
        self.button1 = tk.Button(self, text="Page 1", command=self.page1)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="Page 2", command=self.page2)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="Page 3", command=self.page3)
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self, text="Page 4", command=self.page4)
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
    root.title("My Website")

    # Create a landing page and display it
    landing_page = LandingPage(master=root)
    landing_page.mainloop()
