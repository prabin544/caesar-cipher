  
"""
ord(char) changes letter -> number
chr(num) changes number -> letter
A - 65
Z - 90
a - 97
z - 122
- encrypt(‘abc’,1) would return ‘bcd’ 
- encrypt(‘abc’, 10) would return ‘klm’
- shifts that exceed 26 should wrap around
  - encrypt(‘abc’,27) would return ‘bcd’
def encrypt function
  declare result string
  iterate through each letter 
    declare int_char = ord(letter)
    check for lower or uppercase
    
    if LOWERCASE
      (this means int_char between 97-122)
      keyed = int_char + key
      if keyed is greater than 122
          find out the difference beween keyed and 122
          modulo that difference by 26
          add that difference to 97
          push the result to result string
    if UPPERCASE
      (this means int_char between 65-90)
      keyed = int_char + key
      if keyed is greater than 90
          find out the difference between keyed and 90
          modulo that difference
          add the difference to 65
          push the result to result string
    if its neither
      just add the character to result string
"""


def encrypt(plaintext, key):
    string = ""

    for char in plaintext:

        if char.islower():
            keyed = ord(char) + key
            if keyed > 122 or keyed < 97:
                difference = keyed - 123
                modulo = difference % 26
                string += chr(97 + modulo)
            else:
                string += chr(keyed)

        elif char.isupper():
            keyed = ord(char) + key
            if keyed > 90 or keyed < 65:
                difference = keyed - 91
                modulo = difference % 26
                string += chr(65 + modulo)
            else:
                string += chr(keyed)

        else:
            string += char

    return string


def decrypt(encryptedText, key):
    return encrypt(encryptedText, -key)


# -------------------------------------------------------------------------------

import nltk

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


def crack(encrypted_string):
    """
    - declare encrypted_words_list = encrypted_string split into a list of words
    - declare highest_word_count = the combination with the highest word count. Initialize this with 0
    - declare most_probable_key = the key that gives us the highest word count
    ** there are 25 other possible combinations that could encrypt the string
    ** use encrypt/decrypt(should not matter which one) to test the other 25 combinations using keys 1-26
      for x in range(1,26):
        declare count = 0
        for word in encrypted_words_list
            if decrypted(word, x) in word_list or decrypted(word,x) in name_list:
                count += 1
        if count > highest_word_count:
            highest_word_count = count
            most_probable_key = x
      declare ratio = highest_word_count / word_list_length
      ** now we have the ratio, and the most probable key
      - we can print the ratio and the decrypted string
      - or whatever we're supposed to do in the instructions
    """
    encrypted_words_list = encrypted_string.split()
    highest_word_count = 0
    most_probable_key = 0

    for x in range(1, 26):

        count = 0
        for word in encrypted_words_list:
            if decrypt(word, x) in word_list or decrypt(word, x) in name_list:  # name_list - line 90
                count += 1

        if count > highest_word_count:
            highest_word_count = count
            most_probable_key = x

    probability = highest_word_count / len(encrypted_words_list) * 100
    decrypted_word = decrypt(encrypted_string, most_probable_key)

    print(f"Decryption Probability: {probability}%")
    print(f"Most Probable Key: {most_probable_key}")
    return decrypted_word


if __name__ == "__main__":

    # input1 = "ABCD"
    # input2 = "abcd"
    # input3 = "ABab"
    # input4 = "AB ab AB cd dfadf  fasdf"
    # input5 = "Hello World. We did it."

    # result1 = encrypt(input5, 900)
    # print(result1)

    # result2 = decrypt(result1, 900)
    # print(result2)

    real_sentence = "It was the best of times, it was the worst of times."
    encrypted = encrypt(real_sentence, 18)

    result6 = crack(encrypted)
    print(result6)
