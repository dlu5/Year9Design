from tkinter import *

def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)
    
def addItem():
    item = entry.get()
    if (lst.count(item) == 0):
        lst.append(item)
        entry.delete(0, END)
        updatelab()
        
def removeItem():
    item = entry.get()
    if (lst.count(item) !=0):
        lst.remove(item)
        entry.delete(0, END)
        updatelab()
        
# these are our variables       
lst = []
lstprint = ""

root = Tk()

# gives sizes and position of labels 0 and 900 are the x and y
root.geometry("300x400+0+900")
root.title("hockey pool")

instlab = Label(root,text="Input (e.g., McDavid,Connor):")
instlab.config(background="blue")
instlab.config(foreground="white")
instlab.pack()

# Entry is a entry widget
entry = Entry(root)
entry.pack()

# adds the "Add" button
addbutton = Button(root, text="Add", fg="blue", command=addItem)

addbutton.pack()

removebutton = Button(root, text="Remove", fg="blue", command=removeItem)
removebutton.pack()

# where to print input
mylab = Label(root, text=lstprint,anchor=W, justify=LEFT)
mylab.pack()



mainloop()