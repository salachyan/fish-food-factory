import tkinter as tk

lst_of_foods = [1,2,3]

#MAKE WINDOW

window = tk.Tk()
def makeWindow():
    window.title("FishFoodFactory")
    window.configure(width = 300, height = 500)


def listFoods():
    frame = tk.Frame()

    for i in range(0,len(lst_of_foods)):
        vari = tk.IntVar()
        tk.Checkbutton(frame,text=lst_of_foods[i],variable=vari).grid(row=i)


makeWindow()
listFoods()



#DISPLAY THE WINDOW
window.mainloop()