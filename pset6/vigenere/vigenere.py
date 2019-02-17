import sys
from cs50 import get_string


def main():
    if len(sys.argv) != 2:
        print("Please enter the program execution command line + one word")
        sys.exit(1)
    else:
        for checker in sys.argv[1]:
            if not checker.isalpha():
                print("enter your key full of alphabet, dont include numbers, spaces etc")
                sys.exit(1)
        key = sys.argv[1]
        plain_text = get_string("Enter your message to be encrypted: ")
        convert_to_cipher(key, plain_text)


def convert_to_cipher(key, text):
    key_checker = 0
    text_checker = 0
    ciphered = ""
    for text_checker in range(len(text)):
        if text[text_checker].isalpha():
            if text[text_checker].isupper():
                character_index = ord(text[text_checker]) - 65  # convert character to ascii number then alphabet index
                if(key[key_checker % len(key)].isupper()):
                    key_number = ord(key[key_checker % len(key)]) - 65  # convert key character to its number value at ascii
                    ciphered_character = (character_index + key_number) % 26  # Given equation
                    ciphered_character += 65
                    ciphered += chr(ciphered_character)
                    key_checker += 1
                    text_checker += 1
                else:  # this case for lowercase characters and above one for upper case
                    key_number = ord(key[key_checker]) - 97
                    ciphered_character = (character_index + key_number) % 26
                    ciphered_character += 65
                    ciphered += chr(ciphered_character)
                    key_checker += 1
                    text_checker += 1
            else:  # this case for character of message that is lowerCase
                character_index = ord(text[text_checker]) - 97
                if(key[key_checker % len(key)].isupper()):
                    key_number = ord(key[key_checker % len(key)]) - 65  # convert key character to its number value at ascii
                    ciphered_character = (character_index + key_number) % 26  # Given equation
                    ciphered_character += 97
                    ciphered += chr(ciphered_character)
                    key_checker += 1
                    text_checker += 1
                else:
                    key_number = ord(key[key_checker % len(key)]) - 97  # convert key character to its number value at ascii
                    ciphered_character = (character_index + key_number) % 26  # Given equation
                    ciphered_character += 97
                    ciphered += chr(ciphered_character)
                    key_checker += 1
                    text_checker += 1
        else:
            ciphered += text[text_checker]
            text_checker += 1
    print(f"ciphertext: {ciphered}")


if __name__ == "__main__":
    main()