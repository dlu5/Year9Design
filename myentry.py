# Imports tkinter module into python so we can use
from tkinter import *
# Master is a variable for window; Tk() makes a window
master = Tk()

# Create this method before you create the entry
def return_entry(en):
    """Gets and prints the content of the entry"""
    content = entry.get()
    
    if(content != ""):
        print(content)
        
    entry.delete(0, END)
     
    # Changes str to int
    content = int(content)
    
    # Input is squared
    print(content * content)
    
    
Label(master, text="Input: ").grid(row=0, sticky=W)

# Tells which window to put the entry in
entry = Entry(master)

# Tells where the entry is: row 0 and 1st column
entry.grid(row=0, column=1)

# Connect the entry with the return button
entry.bind('<Return>', return_entry)

# Keeps window open
mainloop()

