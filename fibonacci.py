f1 = 0
f2 = 1 #first and second fibonacci numbers printed before the for loop
print(f1,end=",") 
print(f2,end=",")

for i in range(2,100): #since we printed the first two numbers we start our range at 2
     fib = f1 +f2
     f1 = f2
     f2 = fib
     print(fib,end=",")
input("Press Enter")

