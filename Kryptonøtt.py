# TODO clean code up and edit it so it's easier to read

import operator
import itertools

operators = {"encode": operator.add, "decode": operator.sub}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890"'
alphabet_length = len(alphabet)

# DESCRIPTION  either encodes or decodes a message depending of user input. The key makes each message encoded unique
def vigenere_encryption(msg, key, operator):
    encoded_word = ''

    key_length = len(key)
    encode_decode = operator
    operator_function = operators[encode_decode]


    for i, char in enumerate(msg):
        # Finds the position of the char
        msgint = alphabet.find(char)
        '''
        Finds the position of the letter corresponding to the index in keyword.
        For example, if i = 3 and len(keyword) = 6 would give 2, leaving no rest.
        Then, alphabet.find(key[some_index]) returns a index in the alphabet.
        '''
        encInt = alphabet.find(key[i % key_length])
        if msgint == -1 or encInt == -1:
            return ''
        # Returns the first encrypted letter
        encoded = operator_function(msgint, encInt) % alphabet_length
        # Appends this to the final encoded word
        encoded_word += alphabet[encoded]
    return encoded_word


# DESCRIPTION decodes when you know the length of the key. Generates random keys using itertools.product()
def decode_with_known_key_length(secret_msg, key_length):
    decode_tries = 0
    temp_key = itertools.product("abcdefghijklmnopqrstuvwxyzæøå", repeat=key_length)

    for i in temp_key:
        temp_decode = vigenere_encryption(secret_msg, i, "decode")
        decode_tries += 1

        if temp_decode == message:
            print("-----------------------------------")
            print("Encrypted word -", secret_msg)
            print("Found the word", temp_decode, "with key:", ''.join(i), "after", decode_tries, "tries")
            print("-----------------------------------")
            break
        else:
            pass


# DESCRIPTION decodes a secret message with keywords from key_words.txt
def decode_using_dict(secret_msg):
    # FIXME Seems like if the secret_msg (encoded word) is longer than the keyword, the code wont work.
    message = "Jeg liker kake veldig godt. På den annen side er kake usunt"
    file = open("key_words.txt")
    for line in file:
        temp_decode = vigenere_encryption(secret_msg, line, "decode")
        print(line, temp_decode)

        if temp_decode == message:
            print("-----------------------------------")
            print("Encrypted word -", secret_msg)
            print("Found the word", temp_decode, "with key:", line)
            print("-----------------------------------")
            break
        else:
            pass


# DESCRIPTION console user input function to encode or decode a message
def console_input():
    message = str(input("Enter the string you want encrypted: "))
    keyword = str(input("Enter a desired keyword: "))
    while True:
        operator = str(input("Do you want to decode or encode the word? "))
        if operator != "encode" and operator != "decode":
            print("Invalid input - Should either be 'encode' or 'decode'")
        else:
            break

    vigenere_encryption(message, keyword, operator)


'''
Define variables and fucntions here, for simplicity
'''

message = "K"
key = "aa"

secret = vigenere_encryption(message, key, "encode")
decode_using_dict(message)