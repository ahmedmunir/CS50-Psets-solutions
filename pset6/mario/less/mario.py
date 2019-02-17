from cs50 import get_int


def main():

    # height that will be input by the user and its range from 0 to 23
    height = get_int("Enter the height of mario pyramid: ")

    # check whether he entered valid input or not
    while True:
        if height >= 0 and height <= 23:
            break
        else:
            print("Wrong height, please reneter")
            height = get_int("Enter the height of mario pyramid: ")

    # creating for loop for height
    for i in range(height):
        for j in range((height - i - 1)):
            print(" ", end="")
        for n in range((i + 2)):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()