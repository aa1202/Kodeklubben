alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890"'
print(alphabet.find("a"))
print(alphabet[43])
def vigenere_encode(msg, key):
    secret = ''
    key_length = len(key)
    alphabet_length = len(alphabet)

    for i, char in enumerate(msg):
        #Fins the position of char
        msgInt = alphabet.find(char)
        encInt = alphabet.find(key[i % key_length])
        if msgInt == -1 or encInt == -1:
            return ''
        encoded = (msgInt + encInt) % alphabet_length
        secret += alphabet[encoded]
    return secret

message = 'kodeklubben'
keyword = 'kake'

encrypted = vigenere_encode(message, keyword)

print(encrypted)
def vigenere_decode(codedMsg, key):
    decrypted_message = ""

    for i in range(len(codedMsg)):

        keyPos1 = i %
        keyPos = alphabet.find(key[i])
        cryptPos = alphabet.find(codedMsg[i])



    return decrypted_message



