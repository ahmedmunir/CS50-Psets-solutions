from cs50 import get_float


def main():
    # initlalization of number of coins & check
    no_of_coins = 0
    check = 0

    # getting coins we owed to the customer from him
    coins_owed = get_float("How much change is owed? ")

    # checking whether he entered valid number > 0 or not
    while True:
        if coins_owed > 0:
            break
        else:
            print("Wrong coins!")
            coins_owed = get_float("How much change is owed")

    coins_owed *= 100  # to get the highest number of coins and ignore smalles
    check = round(coins_owed)  # round it to the nearest number to ignore small pennies
    while check % 25 != check:
        check = check - 25
        no_of_coins += 1
    while check % 10 != check:
        check = check - 10
        no_of_coins += 1
    while check % 5 != check:
        check = check - 5
        no_of_coins += 1
    no_of_coins = no_of_coins + check
    print(f"number of coins equal {no_of_coins}")


if __name__ == "__main__":
    main()