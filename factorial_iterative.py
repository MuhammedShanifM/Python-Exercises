factorial=1
num=5
if num<0:
    print("Factorial does not exist")
elif num==0:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial is",factorial)