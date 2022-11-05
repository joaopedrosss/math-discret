import math
n = int(input())

while True:
    if(n==1):
        break
    prime = True
    n=abs(n)
    div= 2
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0 or n<=1):
            prime=False
            div = i
            break
        
    print("{}\n-----".format(prime)) if prime else print("{}\n{}%{}==0\n-----".format(prime,n,div))
    n = int(input())
