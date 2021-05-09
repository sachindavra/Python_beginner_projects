from random import randint


lottery_number = int(input("Kindly enter lottery number: "))
digits = []


while len(digits) < 3:
    digit = randint(1, 10)
    if digit not in digits:
        digits.append(digit)


if lottery_number not in digits:
    print("you have lost a bet.")
else:
    print("yahh.. you won it. your lottery number %d matches with the output." % lottery_number)