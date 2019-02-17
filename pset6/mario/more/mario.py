from cs50 import get_int


def main():
    # getting height of mario pyramid from the user, and its range from 0 to 23
    height = get_int("please enter height of pyramid: ")

    # checking whether the user entered valid height or not
    while True:
        if height >= 0 and height <= 23:
            break
        else:
            print("Worng height, please renter")
            height = get_int("please enter height of pyramid: ")

    # for loop to draw the pyramid
    for i in range(height):
        for j in range((height - i - 1)):
            print(" ", end="")
        for n in range(i + 1):
            print("#", end="")
        print("  ", end="")
        for n in range(i + 1):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()