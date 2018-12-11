from tkinter import *
"""from tkinter import font"""
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import tkinter as tk

    
def switchPhoto():
    global photo
    my_image = Image.open("headshots/crosbsi01.jpg")
    photo = ImageTk.PhotoImage(my_image)
    can.itemconfig(myimg,image=photo)
    

def create_window():
    window = tk.Toplevel(root)
    display = Label(window, text="Stats: https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")
    display.pack()
    display2 = Label(window, text= "Shooting % is the % of shots on net that result in a goal")
    display2.pack()
    display3 = Label(window, text="Check pts totals the pts of players in roster")
    display3.pack()
    display5 = Label(window, text="Export will export player names as a list in a .txt to specified destination")
    display5.pack()
    

def addValue(value):
    if(lst.count(value) == 0):
        lst.append(value)
        listbox.insert(END, value)

def remplayers(value):
    #if(lst.count(value) != 0):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)
        
'''def updateCan(lstprint):
    first = lstprint.split(",")[1]
    last = lstprint.split(",")[0]
    headshot = "headshots/" + last[0:5] + first[0:2] + "01.jpg"'''

'''if len(lst)>0:
    lstinfor(lst[0])
    first = lst[0].split(",")[1]
    last = lst[0].split(",")[0]
    headshot = "headshots/" + last[0:5] + first [0:2] + "01.jpg"
    
else:
    headshot="headshots/marnemi01.jpg"'''
        
        
def makeList():
    if content != -99:
        names=content.findAll(attrs={"data-stat" : "player"}) #"data-stat" : "team_id"
    playerlist = []
    for player in names:
        if (player.get('csk') != "None"):
            playerlist.append(player.get('csk'))
    return playerlist
        
def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
    
def saveasList():
    root.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Select file")
    
    myfile = open(root.filename, "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    
    print (root.filename)
    messagebox.showinfo("myplayers.txt", "Players saved to disk")

   
def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)
        
def removeItem(value):
    items = listbox.curselection()
    pos = 0
    for i in items:
        idx = int(i) - pos
        listbox.delete(idx,idx)
        pos = pos + 1
        
def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
        
# loop to check my players
    for myplayer in lst: 
        dTag = content.find(attrs={"csk": myplayer})
        parent = dTag.findParent("tr")
        playerpts = int(parent.contents[8].text) # 8th tag is total points
        print(myplayer + " " + str(playerpts))
        totalpts=0
        totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
     
def createlistbox(value):
    global image1
    global photo
    var=listbox.get(ANCHOR)
    filename = str(var)


    
# when you find a comma split it there
    a,b = filename.split(",")
    filename = a[0:5].lower() + b[0:2].lower() + "01.jpg"
    image1 = Image.open("headshots/" + filename)
    photo = ImageTk.PhotoImage(image1)
    can.create_image(8,8, anchor=NW, image=photo)
    
    if var!=None:
        dTag=content.find(attrs={"csk":var}) 
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        rank=int(parent.contents[0].text) 
        age=int(parent.contents[2].text)
        team=str(parent.contents[3].text)
        position=str(parent.contents[4].text)
        gp=int(parent.contents[5].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        pm=int(parent.contents[9].text)
        sg=int(parent.contents[19].text)
        sp=str(parent.contents[20].text)
         
        
        
    listbox2 = Listbox(root, height=14)
    listbox2.place(x=200, y=251)
    listbox2.insert(END, "Rank: " + str(rank))
    listbox2.insert(END, "Team: " + (team))
    listbox2.insert(END, "Position: " + (position))
    listbox2.insert(END, "Age: " + str(age))
    listbox2.insert(END, "Points: "+ str(points))
    listbox2.insert(END, "+/-: "+ str(pm))
    listbox2.insert(END, "Games Played: "+ str(gp))
    listbox2.insert(END, "Goals: "+ str(goals))
    listbox2.insert(END, "Assists: "+ str(assists))
    listbox2.insert(END, "Shots On Goal: "+ str(sg))
    listbox2.insert(END, "Shooting %: "+ str(sp))




root = Tk()
root.geometry("590x600+3+900")
root.configure(background="white")
root.title("Daniel Lu Hockey Pool")
l = Listbox(root) 

can = Canvas(root,width=125, height=180,)
image1 = Image.open('headshots/armiajo01.jpg')
# image1.putalpha(1)
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)


# draw canvas
can = Canvas(root, width=500, height=225)
can.grid(row=0, column=0, padx=10, pady=10)
image2 = Image.open("realhockey.png")
photo = ImageTk.PhotoImage(image2)
can.create_image(0, 0, anchor=NW, image=photo)


'''image1 = Image.open('headshots/armiajo01.jpg')
# image1.putalpha(1)
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)'''

can.create_oval(20, 10, 120, 110, fill="cyan", outline="#DDD", width=5)
can.create_line(20, 60, 120, 60, fill="#DDD", width=20)
can.create_text(70,60, text="pool", fill="white")


# these are our variables       
lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get("https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99


# listbox
listbox = Listbox(root, height=14)
listbox.grid(row=1, column=0, sticky=NW, padx=12)
listbox.insert(END, )


listbox.bind('<<ListboxSelect>>',createlistbox)
listbox.bind('<Double-Button>',remplayers)


# pulldown
OPTIONS = makeList()
variable = StringVar(root)
variable.set(OPTIONS[0]) #default value
w = OptionMenu(root, variable, *OPTIONS, command=addValue)
w.place(x=430, y=253)


f = open("myplayers.txt", "r")
cont = f.read()
print(cont)
cont=cont.split("\n")
for saveplayer in cont:
    if (cont != 1):
        listbox.insert(END,saveplayer)
        lst.append(saveplayer)
        f.close()
    

#print(list)

# adds save button
savebutton = Button(root, text="Save", fg="green", command=saveList)
savebutton.place(x=432, y=280)

#adds save as button
saveasbutton = Button(root, text="Export", fg="blue", command=saveasList)
saveasbutton.place(x=432, y=300)

# adds remove button
'''removebutton = Button(root, text="Remove", fg="red", command=removeItem)
removebutton.place(x=450, y=320)'''


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



c = tk.Button(root, text="tutorial/help", command=create_window, fg="red")
c.grid(row=4, column=0, sticky=NW, padx=12)




mainloop()