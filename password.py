# password.py - lets user try to match password 3 times

secret = "joe"

i = 100

# i will always be >1 because it is 100 so infinite loop

while (i>1):
    pword = input("enter a number: ")
	
    if (secret == pword):
        print("welcome")
        break
    else:
        print("incorrect ... ")