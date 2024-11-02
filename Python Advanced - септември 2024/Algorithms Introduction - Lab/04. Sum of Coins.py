def choose_coins(needed_money, *coins_list):
    coins_list = list(coins_list)
    coins_list.sort(reverse=True)
    index = 0
    used_coins = {}

    while needed_money > 0 and index < len(coins_list):
        count_coins = needed_money // coins_list[index]
        needed_money %= coins_list[index]

        if count_coins > 0:
            used_coins[coins_list[index]] = count_coins

        index += 1

    if needed_money != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for coin, count in used_coins.items():
            result += f"{count} coin(s) with value {coin}\n"

        return result


coins = [int(x) for x in input().split(", ")]
target = int(input())
print(choose_coins(target, *coins))
