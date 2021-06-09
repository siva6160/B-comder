num=int(input(""))
r=0
sum=0
temp=num
for i in range(1,num):
    r=num%10
    sum=(sum*10)+r
    num=num//10
print(sum)
    
#if(temp==sum):
    #print("polindrime")
#else:
    #print("not")
    

