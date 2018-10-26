from tkinter import *
master = Tk()

def return_entry(en):
    content = entry.get()
    num = int(content)
    
if(num<100):
    print("<100")  
      
elif(num>100):
    print(">100")
      
else:
    print("=100")
    
mainloop()