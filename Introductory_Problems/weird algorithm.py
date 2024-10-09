num = int(input())

if 1<=num<=10**6: 
    ls = []
    ls.append(num)
    while ls[-1] > 1:
        num = ls[-1]
        if num%2 == 0:
            num //=2
            ls.append(num)        
        else:
            num*=3
            num+=1
            ls.append(num)
    print(' '.join(map(str,ls)))
else:
    print("Please enter a number between 1 and 10^6 ")

