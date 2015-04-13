# TODO clean code up and edit it so it's easier to read

import operator
import itertools
import sys
import time

operators = {"encode": operator.add, "decode": operator.sub}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890"'
alphabet_length = len(alphabet)

def vigenere_encryption(msg, key, operator):
    '''
    Either encodes or decodes a message depending of user input. The key makes each message encoded unique
    '''
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


def decodeWithKnownMessage(secret_msg, max_key_len):
    '''
    Decodes when you know the length of the key and known length of message.
    '''

    for keyLen in range(max_key_len):
        if keyLen != 0:
            temp_key = itertools.product("abcdefghijklmnopqrstuvwxyzæøå", repeat=keyLen)
            for i in temp_key:
                temporarily_encrypted_message = vigenere_encryption(secret_msg, i, "decode")

                if temporarily_encrypted_message == message:
                    print("-----------------------------------")
                    print("Encrypted word -", secret_msg)
                    print("Found the word", temporarily_encrypted_message, "with key:", ''.join(i))
                    print("-----------------------------------")
                    sys.exit()
                else:
                    #Means that the temporarily_encrypted_message did not match the message
                    pass
            else:
                pass
        else:
            pass


def decodeUnknownKey(secret_msg, max_key_length, blank_space):
    '''
    Decodes a secret message with not knowing the length of the key or the message it self
    Limits the outcomes by checking for the number of occurrences of spaces, and stores this in a list for manual
    checking. For instance, if blank_space is < 3 the list will get very long consisting of sentences with spaces if
    the key is 5 or more in length. On the other hand, it is important that blank_space doesn't exceed the actual
    number of spaces in the original sentence.
    '''

    white_space_count = 0
    connected_letters_count = 0
    valid_decryptions = []

    for keyLen in range(max_key_length):
        if keyLen != 0:
            print("Trying to decrypt with key length", keyLen)
            temp_key = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=keyLen)
            for i in temp_key:
                temporarily_encrypted_message = vigenere_encryption(secret_msg, i, "decode")
                if "kake" in temporarily_encrypted_message:
                    white_space_count += 1
                    valid_decryptions.append(temporarily_encrypted_message)
                else:
                    connected_letters_count += 1

            else:
                pass
        else:
            pass
    print("Number of whitespaces:", white_space_count)
    print("Number of connected letters:", connected_letters_count)

    for element in valid_decryptions:
        print(element)


def decodeKnownKeyLength(secret_msg, key_length, blank_space):
    '''
    Decodes a message with known keyword length, and does not require original decoded message.
    Limits the outcomes by checking for the number of occurrences of spaces, and stores this in a list for manual
    checking. For instance, if blank_space is < 3 the list will get very long consisting of sentences with spaces if
    the key is 5 or more in length. On the other hand, it is important that blank_space doesn't exceed the actual
    number of spaces in the original sentence.
    '''

    white_space_count = 0
    connected_letters_count = 0
    valid_decryptions = []

    print("Trying to decrypt with key length", key_length)
    temp_key = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=key_length)

    decode_start = time.time()
    for i in temp_key:
        temporarily_encrypted_message = vigenere_encryption(secret_msg, i, "decode")
        if "programming" in temporarily_encrypted_message and temporarily_encrypted_message.count(" ") >= blank_space:
            white_space_count += 1
            print(temporarily_encrypted_message)
        else:
            connected_letters_count += 1
    decode_end = time.time()
    print("Decoded string with every key in", ((decode_end - decode_start)/60), "minutes")

    print_stats = str(input("Should I print out the stats? (Y/N) ")).lower()
    if print_stats == "y":
        print("Number of whitespaces:", white_space_count)
        print("Number of connected letters:", connected_letters_count)
    else:
        pass

    for element in valid_decryptions:
        print(element)


def decode_using_dict(secret_msg, blank_space):
    '''
    Decodes a message using a dictionary, and demands the knowing of decoded message in order to check if it is correct
    '''
    white_space_count = 0
    connected_letters_count = 0


    file = open("key_words.txt")
    for line in file:
        temp_decode = vigenere_encryption(secret_msg, line.strip(), "decode")

        if " " in temp_decode and temp_decode.count(" ") >= blank_space:
            white_space_count += 1
            print("Encrypted message:", temp_decode)
            print("Key:", line)
        else:
            connected_letters_count += 1

def console_input():
    '''
    Console input for encoding a message
    '''
    # TODO further build upon this function so the user can decode a word
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
secret = 'q0Ø:;AI"E47FRBQNBG4WNB8B4LQN8ERKC88U8GEN?T6LaNBG4GØ""N6K086HB"Ø8CRHW"+LS79Ø""N29QCLN5WNEBS8GENBG4FØ47a'
decodeKnownKeyLength(secret,6,14)
FOUND THE SECRET! If debugging is the process of removing bugs, then programming must be the process of putting them in.
'''

secret = 't-JO:BK0aM,:CQ+ÆAGW?FJGB0KVCGMQ6SQN"GAIDL-PÅ7954E:7Jr,IÆoCF0M"CQdØVlHD53CÅ;IA2DMG5ØHDØVåL:JQØ439LRBBVEMTBÆ6CF0M"CQNAG8G1V6LÅ8FF4Z'
decode_using_dict(secret, 13)

#KEYWORDS FROM http://www.mieliestronk.com/wordlist.html