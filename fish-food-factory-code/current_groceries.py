from tkinter import *
new_foods = ["lemon", "cilantro", "cookie"]
root = Tk()
root.geometry("400x400")
root.title(" Q&A ")
label = Text(root)
for i in new_foods: 
    label.insert(END,i+'\n')
    label.pack()

 
mainloop()
