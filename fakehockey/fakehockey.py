from tkinter import *
"""from tkinter import font"""
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup


def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()b
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
    
def saveasList():
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
        
"""def removeItem():
    item = entry.get()
    if (lst.count(item) !=0):
        lst.remove(item)
        entry.delete(0, END)
        updatelab()"""
        
def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    
    if site.status_code is 200:
        content = BeautifulSoup(site.content, "html.parser")
        totalpts = 0
        for myplayer in listbox: #loop to check my players
            dTag = content.find(attrs={"csk": myplayer})
            parent = dTag.findParent("tr")
            playerpts = int(parent.contents[8].text) # 8th tag is total points
            print(myplayer + " " + str(playerpts))
            totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
        

root = Tk()
root.geometry("530x600+3+900")
root.configure(background="white")
root.title("Fake Hockey Pool Prototype")

# draw canvas
can = Canvas(root, width=500, height=225)
can.grid(row=0, column=0, padx=10, pady=10)
image1 = Image.open("fakehockey.png")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(20, 10, 120, 110, fill="cyan", outline="#DDD", width=5)
can.create_line(20, 60, 120, 60, fill="#DDD", width=20)
can.create_text(70,60, text="fake pool", fill="white")


# these are our variables       
lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get("https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")

# listbox
listbox = Listbox(root, height=7)
listbox.grid(row=1, column=0, sticky=NW, padx=10)
listbox.insert(END, "Crosby,Sidney")

# pulldown
OPTIONS = ["Crosby,Sidney","McDavid,Connor"]
variable = StringVar(root)
variable.set(OPTIONS[0]) #default value
w = OptionMenu(root, variable, *OPTIONS)
w.grid(row=1, column=0, sticky=NE, padx=10)

# adds save button
savebutton = Button(root, text="Save", fg="green", command=saveList)
savebutton.place(x=450, y=280)

#adds save as button

saveasbutton = Button(root, text="Save as", fg="springgreen2", command=saveasList)
saveasbutton.place(x=450, y=300)

# adds the "Add" button
addbutton = Button(root, text="Add", fg="blue", )
addbutton.place(x=450, y=320)

# adds remove button
removebutton = Button(root, text="Remove", fg="red",)
removebutton.place(x=450, y=340)

# where to print input
mylab = Label(root, text=lstprint,anchor=W, justify=LEFT)
mylab.grid()

# Label for checking pts
mylab = Label(root, text=lstprint,anchor=W,justify=LEFT)
mylab.grid()

ptsbutton = Button(root, text = "Check pts", command=scrape)
ptsbutton.grid()

mypts = Label(root,text=totalpts)
mypts.grid()




mainloop()