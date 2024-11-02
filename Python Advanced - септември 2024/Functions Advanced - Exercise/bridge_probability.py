from math import comb

def probability_of_k_cards(k):
    total_ways = comb(52, 13)  # Общ брой начини да изберем 13 карти от 52
    ways_for_k_cards = comb(13, k) * comb(39, 13 - k)  # Начини за избор на k карти от една боя
    probability = ways_for_k_cards / total_ways  # Вероятността
    return probability

# Пример: изчисляване на вероятностите за 0 до 13 карти от една боя
for k in range(14):
    prob = probability_of_k_cards(k)
    print(f"Вероятност да получим {k} карти от една боя: {prob}")