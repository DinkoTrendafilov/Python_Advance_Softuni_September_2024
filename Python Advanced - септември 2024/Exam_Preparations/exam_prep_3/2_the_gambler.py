n = int(input())

matrix = []
gambler_position = ()
initial_money = 100

for row in range(n):
    current_row = list(input())
    matrix.append(current_row)
    if "G" in current_row:
        gambler_position = (row, current_row.index("G"))

direction_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    if command == "end":
        print(f"End of the game. Total amount: {initial_money}$")
        break
    direction = command

    new_row = gambler_position[0] + direction_mapper[direction][0]
    new_col = gambler_position[1] + direction_mapper[direction][1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        initial_money = 0
        print("Game over! You lost everything!")
        break

    matrix[gambler_position[0]][gambler_position[1]] = "-"
    gambler_position = (new_row, new_col)

    element = matrix[new_row][new_col]

    if element == "W":
        initial_money += 100

    elif element == "P":
        initial_money -= 200

    elif element == "J":
        initial_money += 100_000
        matrix[new_row][new_col] = "G"
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {initial_money}$")
        break

    if initial_money <= 0:
        initial_money = 0
        print("Game over! You lost everything!")
        break
    matrix[new_row][new_col] = "G"

if initial_money > 0:
    for row in matrix:
        print("".join(row))
