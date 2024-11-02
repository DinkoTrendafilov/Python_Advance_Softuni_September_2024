n = int(input())
board = [list(input()) for _ in range(n)]

gambler_position = ()
for row in range(n):
    if 'G' in board[row]:
        gambler_position = (row, board[row].index('G'))

amount = 100

directions_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "end":
        print(f"End of the game. Total amount: {amount}$")
        break

    new_row = gambler_position[0] + directions_mapper[command][0]
    new_col = gambler_position[1] + directions_mapper[command][1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        print("Game over! You lost everything!")
        break

    current_cell = board[new_row][new_col]
    board[gambler_position[0]][gambler_position[1]] = '-'
    gambler_position = (new_row, new_col)

    if current_cell == "W":
        amount += 100
    elif current_cell == "P":
        amount -= 200
    elif current_cell == "J":
        amount += 100000
        board[new_row][new_col] = 'G'
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {amount}$")
        break

    if amount <= 0:
        print("Game over! You lost everything!")
        break

    board[new_row][new_col] = 'G'

if amount > 0:
    for row in board:
        print("".join(row))
