class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = input().split(", ")
pin_code = int(pin_code)
balance = float(balance)
age = int(age)

LEGAL_AGE = 18

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("#")
    action = split_command[0]

    if age < LEGAL_AGE:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    if action == "Send Money":
        send_money = float(split_command[1])
        if send_money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        needed_pin_code = int(split_command[2])
        if needed_pin_code != pin_code:
            raise PINCodeError("Invalid PIN code")

        balance -= send_money
        print(f"Successfully sent {send_money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        salary = float(split_command[1])
        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        else:
            salary /= 2
            print(f"{salary:.2f} money went straight into the bank account")
