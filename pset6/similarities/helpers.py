from nltk.tokenize import sent_tokenize, word_tokenize
from time import sleep


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    file1 = a.splitlines()  # split the first string into list of strings
    file2 = b.splitlines()  # split the second string into list of strings
    result = []
    checker = 0  # will be used to avoid duplicate.
    # loop through each element inside 2 lists
    for i in file1:  # for loop through the first file
        for j in file2:  # for loop through the 2nd file
            if i == j:
                for k in result:
                    if i == k:
                        checker = 1
                if checker == 0:
                    result.append(i)
                    break
                checker = 0
    return result


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    file1 = sent_tokenize(a)  # divide first file into sentences
    file2 = sent_tokenize(b)  # divide second file into sentences
    result = []
    checker = 0  # will be used to avoid duplicate.
    # loop through each element inside 2 lists
    for i in file1:  # for loop through the first file
        for j in file2:  # for loop through the 2nd file
            if i == j:
                for k in result:
                    if i == k:
                        checker = 1
                if checker == 0:
                    result.append(i)
                    break
                checker = 0
    return result


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    # divide each long string into words
    file1 = word_tokenize(a)
    file2 = word_tokenize(b)
    result = []
    checker = 0
    n = int(n)
    # getting list of substrings of first file
    new_file1 = new_list(file1, n)
    # getting list of substrings of second file
    new_file2 = new_list(file2, n)
    # loop through each element inside 2 lists
    for i in new_file1:  # for loop through the first file
        for j in new_file2:  # for loop through the 2nd file
            if i == j:
                for k in result:
                    if i == k:
                        checker = 1
                if checker == 0:
                    result.append(i)
                    break
                checker = 0
    return result


# return the substrings of all list
def new_list(file, n):
    # define the left cursor and right cursor of each string to be printed
    left = 0
    right = n
    # last list that will be returned after making all substrings
    last_list = []
    for i in file:
        while True:
            # here if the input number greater than string length, so we will ignore that string
            if n > len(i):
                break
            last_list.append(i[left:right])
            # check if we reach the end of word or not
            if right >= len(i):  # right >= len(i) here to avoid stuck at '' empty string
                left = 0
                right = n
                break
            left += 1
            right += 1
    return last_list
