#Implementation of Caesar cipher.

#the details of Caesar cipher can be found here . https://en.wikipedia.org/wiki/Caesar_cipher

#encryption function
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            shifted_char_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a')
            result += chr(shifted_char_code)
        else:
            result += char

    return result

#decryption function

def decrypt(text, shift):
    return encrypt(text, -shift)

#get the user choice based on the input number.
def get_user_choice():
    while True:
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("-1. Quit")
        choice = input("Enter 1, 2, or -1: ")

        if choice in ['1', '2', '-1']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or -1.")


#get the plain text and desired key, also throw exception in case of non-integer key.
def get_text_and_key():
    while True:
        text = input("Enter the text: ")
        key_str = input("Enter the key: ")

        try:
            key = int(key_str)
            return text, key
        except ValueError:
            print("Invalid key. Please enter an integer.")

def main():
    while True:
        choice = get_user_choice()

        if choice == 1:  # Encrypt
            plaintext, key = get_text_and_key()
            result = encrypt(plaintext, key)
            print("Encrypted text:", result)
        elif choice == 2:  # Decrypt
            ciphertext, key = get_text_and_key()
            result = decrypt(ciphertext, key)
            print("Decrypted text:", result)
        elif choice == -1:  # Quit
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()
