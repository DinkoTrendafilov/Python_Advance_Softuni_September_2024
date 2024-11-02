from itertools import combinations


def find_combinations(arr, target_sum):
    found_combinations = []

    for r in range(2, len(arr) + 1):
        for comb in combinations(arr, r):
            if sum(comb) == target_sum:
                found_combinations.append(comb)

    if found_combinations:
        print(f"Combinations that sum up to {target_sum}:")
        for comb in found_combinations:
            print(f"{' + '.join(map(str, comb))} = {target_sum}")
    else:
        print(f"No combinations found that sum up to {target_sum}.")


numbers = [1, 2, 3, 4, 5, 6, 7]
desired_sum = 9
find_combinations(numbers, desired_sum)
