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

 
mainloop()
