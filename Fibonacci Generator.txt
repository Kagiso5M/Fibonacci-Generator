#Auther: Kagiso Peter Motsisi
#Internship Type: Python Programming
#Title: Fibonacci Generator

#Fibonacci Function
def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

#User sets the fibonacci liit
limit = input("Please enter the limit:\n")
print(f'The limit entered is:{limit}')
limit = int(limit)

#Printing results
print(f'your pattern is as follows: ')
for i in fib():
    if i > limit:   
         break;
    print(i)
