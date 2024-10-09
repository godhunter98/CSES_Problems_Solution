n = int(input())

ls_even = []
ls_odd = []


if n==2 or n==3:
    print('NO SOLUTION')
else:
    for i in range(1,n+1):   
        if i%2 == 0:
            ls_even.append(i)
        else:
            ls_odd.append(i)

    ls_even.extend(ls_odd)  
    if len(ls_even)==0:
        print('NO SOLUTION')
    else:
        print(' '.join(map(str,ls_even)))
