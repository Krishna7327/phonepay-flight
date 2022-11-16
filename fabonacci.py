#program for fibonacci series
def fibonacci(number):
    if number<0:
        print("enter the valid input:")
    elif number==0:
        return 0
    elif number==1 or number==2:
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1)
number=int(input("enter the range:"))
for n in range(number):
    
    print(fibonacci(n))
