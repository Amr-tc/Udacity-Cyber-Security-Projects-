#Function to define caeser cipher
def caesar_cipher(text, shift):
    result = ""
    #for loop to check each character in the text
    for char in text:
        # If condition to check if the letter is Alphabet
        if char.isalpha():
            ascii_code = ord(char)
            #shifting the character
            shifted_ascii = ascii_code + shift
            # If condition for the upper case letters
            # To prevent replacing with non-alphabetic characters and return from the Beginning
            if char.isupper():
                while shifted_ascii > ord('Z'):
                    shifted_ascii -= 26
                while shifted_ascii < ord('A'):
                    shifted_ascii += 26
            # If condition for the lower case letters
            elif char.islower():
                while shifted_ascii > ord('z'):
                    shifted_ascii -= 26
                while shifted_ascii < ord('a'):
                    shifted_ascii += 26
            result += chr(shifted_ascii)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

if __name__ == "__main__":
    shift = 3  # The fixed number of positions to shift

    # Read the plaintext from input.txt
    with open("input.txt", "r") as file:
        plaintext = file.read()

    # Apply the Caesar cipher for encryption
    encrypted_text = caesar_cipher(plaintext, shift)
    print("Encrypted Text:\n", encrypted_text)

    # Write the encrypted text to encrypted.txt
    with open("encrypted.txt", "w") as file:
        file.write(encrypted_text)

    # Decrypt the encrypted text
    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("\nDecrypted Text:\n", decrypted_text)

    # Write the decrypted text to decrypt.txt
    with open("decrypt.txt", "w") as file:
        file.write(decrypted_text)
