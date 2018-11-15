from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    root.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Select file")
    print (root.filename)
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
    
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
        
def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    
    if site.status_code is 200:
        content = BeautifulSoup(site.content, "html.parser")
        totalpts = 0
        for myplayer in lst: #loop to check my players
            dTag = content.find(attrs={"csk": myplayer})
            parent = dTag.findParent("tr")
            playerpts = int(parent.contents[8].text) # 8th tag is total points
            print(myplayer + " " + str(playerpts))
            totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
    
        
# these are our variables       
lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get("https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")

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

# adds remove button
removebutton = Button(root, text="Remove", fg="red", command=removeItem)
removebutton.pack()

savebutton = Button(root, text="Save", fg="springgreen2", command=saveList)
savebutton.pack()

# where to print input
mylab = Label(root, text=lstprint,anchor=W, justify=LEFT)
mylab.pack()

# Label for checking pts
mylab = Label(root, text=lstprint,anchor=W,justify=LEFT)
mylab.pack()

ptsbutton = Button(root, text = "Check pts", command=scrape)
ptsbutton.pack()

mypts = Label(root,text=totalpts)
mypts.pack()




mainloop()