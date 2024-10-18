n = int(input())

if 1 <= n <= 10**6:
    x = [x for x in range(1, n + 1)]
    i = len(x)
    sum_first_x_terms = (i / 2) * (2 * x[0] + (i - 1))

    if sum_first_x_terms % 2 != 0:
        print("NO")
    else:
        print("YES")
        set_1 = []
        set_2 = []

        target = sum_first_x_terms // 2

        current_sum = 0

        for i in range(n, 0, -1):
            if current_sum + i <= target:
                set_1.append(i)
                current_sum += i
            else:
                set_2.append(i)

        print(len(set_1))
        print(" ".join(map(str, set_1)))
        print(len(set_2))
        print(" ".join(map(str, set_2)))

# we wrote this piece of code to check if the sum of first n numbers in a list can be equal to the last n
# Total = 0
# Total_sum = sum(x)
# for i in range(len(x)):
#     Total += x[i]
#     if Total == Total_sum - Total:
#         print("Total Matches at index", i)
#         break
# else:
#     print("No Match Found")
# print(Total)
