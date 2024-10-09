size = int(input())
array = str(input()).split(' ')
array = [int(i) for i in array]

if 1<=size<=2*(10**5):
    moves = 0
    for i in range(size-1):
        if array[i] > array[i+1]:
            moves+=(array[i]-array[i+1])
            array[i+1]=array[i]
print(moves)