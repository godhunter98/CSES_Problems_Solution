n =  int(input())  # Capture the number of test cases (this is now used)
text = [input() for _ in range(n)]  # Capture each test case line separately

def coin_movement_possible(coins_in_left_pile: int, coins_in_right_pile: int):
    if (coins_in_left_pile + coins_in_right_pile) % 3 == 0 and max(coins_in_left_pile, coins_in_right_pile) <= 2 * min(coins_in_left_pile, coins_in_right_pile):
        print('YES')
    else:
        print('NO')

for i in text:
    if i:  # Check to avoid processing empty lines
        a, b = i.split(' ')
        a = int(a)
        b = int(b)
        coin_movement_possible(a, b)
  # Capture all the remaining lines as a single string and split by newlines