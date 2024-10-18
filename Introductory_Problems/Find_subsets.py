def get_subsets(n, current_subset):
    if n == 0:
        return [current_subset]
    exclude_n = get_subsets(n - 1, current_subset)

    include_n = get_subsets(n - 1, current_subset + [n])

    return exclude_n + include_n


print(get_subsets(20, []))

sum_groups = {}
for i in get_subsets(6, []):
    sublist_sum = sum(i)

    if sublist_sum in sum_groups:
        sum_groups[sublist_sum].append(i)

    else:
        sum_groups[sublist_sum] = [i]

for key, value in sum_groups.items():
    if len(value) > 1:
        print(f"Sublists with sum {key}: {value}")
