single = int(input())
sequence = str(input()).split(' ')

if 2<= single <= 2*(10**5):
    sum_sequence = sum(int(x) for x in sequence)
    sum = (single * (single+1))//2
    print(sum-sum_sequence)
else:
    pass