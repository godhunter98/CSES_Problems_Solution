x = int(input())

for n in range(1, x + 1):
    total_ways = ((n * n) * ((n * n) - 1)) / 2
    attacking_ways = 2 * ((n - 2) * (n - 1) * 2)
    net_ways = total_ways - attacking_ways
    print(int(net_ways))
