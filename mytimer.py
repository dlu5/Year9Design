'''
mytimer.py - a program to test the speed of your computer
daniel.lu - original conding, sept 21, 2018

(This is a banner)
'''

# import timeit module
# only import the function required (default_timer)
# speeds up your code

from timeit import default_timer as timer

# defining a function called mytimer
def mytimer():

    start = timer()
    print(start)
    
    for i in range (1000000):
        print(i)		
	
    end = timer()
    print(end)
    
    print(end - start)	
	
# calling or invoking the function mytimer
mytimer()