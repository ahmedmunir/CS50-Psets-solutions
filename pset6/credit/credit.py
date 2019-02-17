from cs50 import get_int


def main():
    # initialization of important parameters we need
    cardNumber = 0
    x, y, z, x1, x2 = 0, 0, 0, 0, 0
    counter = 0  # to count how many digits be eliminated
    calculator = 0  # to calculate the num of all numbers
    # get the card Number from the user
    cardNumber = get_int("Enter your credit card Number: ")
    # check whether the user enter valid number or not
    while True:
        if cardNumber:
            break
        else:
            cardNumber = get_int("Enter your credit card Number: ")
    # divide card number by 100 and compare it to 10 to know when we reach to last 2 or 3 digits
    while (cardNumber // 100) > 10:
        x = cardNumber % 100
        # this will be used at condition of last 2 digits are 05 or 0 any number.
        if x < 10:
            calculator += x
        else:
            y = x % 10  # y responsible of getting last digit
            x = x // 10  # x here responsible of getting second to last digit
            x = x * 2
            # this will be used to convert x*2 to first digit + second digit if x*2 >=10
            if x >= 10:
                x1 = x % 10
                x2 = x // 10
                x = x1 + x2
            # getting the result of multiply second to last digit by 2 and add it to last digit
            z = x + y
            calculator += z
        cardNumber = cardNumber // 100
        counter += 2
    # check for VISA or AMEX
    if (cardNumber > 100) and (counter == 10) or (cardNumber > 100) and (counter == 12):
        x = cardNumber % 10
        calculator += x
        y = cardNumber // 10
        if y == 34.0 and counter == 12 or y == 37.0 and counter == 12:
            x = y % 10
            x = x * 2
            if x > 10:
                x1 = x % 10
                x2 = x // 10
                x = x1 + x2
            calculator += x
            y = y // 10
            calculator += y
            if calculator % 10 == 0:
                print("AMEX")
            else:
                print("INVALID")
        elif (cardNumber % 100) == 4 and (counter == 10):
            x = y % 10
            x = x * 2
            if x > 10:
                x1 = x % 10
                x2 = x // 10
                x = x1 + x2
            calculator += x
            y = y // 10
            calculator += y
            if calculator % 10 == 0:
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")
    elif (cardNumber < 100) and (counter == 14):
        y = cardNumber % 10
        x = cardNumber // 10
        x = x * 2
        if x >= 10:
            x1 = x % 10
            x2 = x // 10
            x = x1 + x2
        calculator += y
        calculator += x
        if calculator % 10 == 0:
            if cardNumber == 51 or cardNumber == 52 or cardNumber == 53 or cardNumber == 54 or cardNumber == 55:
                print("MASTERCARD")
            elif cardNumber // 10 == 4:
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()