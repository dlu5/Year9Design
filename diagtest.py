# get user input using inpu() function
num = input("enter a num: ")
num = int(num)
# converting/casting string to a num
# could also do: num = int(input("enter a num: ")) but may be less readable

mylist = [1,2,3,4,5]

# don't need to define "n" because the variable is auto assigned every integer in the list 
for n in mylist:
    if (n == num):
        # string concatenation; not strings and ints and floats
        print(" you found it " + str(num))
        break
    else:
        print(str(num) + " is not equal to " + str(n))