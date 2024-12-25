#Auther: Kagiso Peter Motsisi
#Internship Type: Python Programming
#Title: Fibonacci Generator

#Fibonacci Function
def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y
#Printing results
for i in fib():
    if i > 5000:   #5000 is the number that should not be crossed_over
         break;
    print(i)