<<<<<<< HEAD
import tkinter as tk
from PIL import Image, ImageTk
=======
from tkinter import *
new_foods = ["lemon", "cilantro", "cookie"]
root = Tk()
root.geometry("400x400")
label = Text(root)
  
bgimg= PhotoImage(file = "background.png")
limg= Label(root, i=bgimg)
limg.pack()
for i in new_foods: 
    label.insert(END,i+'\n')
    Font_tuple = ("Comic Sans MS", 20, "bold")
    
# Parsed the specifications to the
# Text widget using .configure( ) method.
    label.configure(font = Font_tuple)
    label.tag_configure("center", justify='center')
    label.insert(1.0, " ")
    label.tag_add("center", "1.0", "end")
    label.pack()
>>>>>>> bfec807c0d8c680f95b3b2a5278e2d3ebd0e7a17

root=tk.Tk()
 
#getting screen width and height of display
#setting tkinter window size
root.geometry("400x400")

new_foods = ["avocado", "cucumber", "onion", "lettuce", "cilantro","rice"]

class Current_Groceries(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas for the background image
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.canvas.place(x=0, y=0)

        # Load and display the background image
        self.configure(bg="#C6E2FF")
                
        for i in new_foods: 

            self.label = tk.Label(self, text=i, font=("Comic Sans MS", 10))
            self.label.pack(pady=10)

if __name__ == "__main__":
    # Create a root window and set its title
    #root = tk.Tk()
    #root.title("Fish Food Factory")

    # Set the window size
    # root.geometry("600x600")

    # Set the window background color
    # root.configure(bg="#FFE6E6")

    # Create a landing page and display it
    landing_page = Current_Groceries(master=root)
    landing_page.mainloop()



