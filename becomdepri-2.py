def isprime():
    if num>1:
        for i in range(2,num):#2
            if(num%i)==0:
                print(num,"not prime Number")
                break;
        else:
             print(num,"prime Number")
num=int(input(""))
prime=isprime()

