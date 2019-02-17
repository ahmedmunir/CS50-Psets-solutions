import sys
from cs50 import get_string


def main():
    # if the user didnt provide the key of program
    if len(sys.argv) != 2:
        print("Notvalid Command line")
        sys.exit(1)
    else:
        # check that the key is valid number
        try:
            int(sys.argv[1])
        except ValueError:
            print("Not valid key")
            sys.exit(1)
        else:
            key = int(sys.argv[1]) % 26  # this modulues to avoid entering number more than 26
            plaintext = get_string("plaintext: ")
            convert_to_cipher(key, plaintext)


def convert_to_cipher(key, text):
    ciphered = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                character_ascii = ord(i) - 65  # ord function to convert character i to its ascii value
                ciphered_character = (character_ascii + key) % 26  # apply equation provided
                last_character = chr(ciphered_character + 65)  # do cipher by convert ascii number of new character to character
                ciphered += last_character
            else:
                character_ascii = ord(i) - 97
                ciphered_character = (character_ascii + key) % 26
                last_character = chr(ciphered_character + 97)
                ciphered += last_character
        else:
            ciphered += i
    print(f"plaintext: {text}")
    print(f"ciphertext: {ciphered}")


if __name__ == "__main__":
    main()