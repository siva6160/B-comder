n=int(input())
print(n,end=" ")

while True:
        if n%2==0:
            n=n//2
            print(n,end="  ")
        elif n%2!=0:
            n=3*n+1
            print(n,end=" ")
        if n==1:
            break
