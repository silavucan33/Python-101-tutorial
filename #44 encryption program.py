# substitution cipher encryption program

import random
import string

#whatever characters you would like to use for your encryption program, list them here as a string.
#however this can be a lot to write, a better solution would be to import some constants from the string module
chars = " " + string.punctuation + string.digits + string.ascii_letters

#im going to turn the string into a list, where each character is an individual element
chars = list(chars)

#to create a copy of a list by using copy method
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

#iterating over every letter in our 'plain_text'
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")


#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

#iterating over every letter in our 'plain_text'
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
