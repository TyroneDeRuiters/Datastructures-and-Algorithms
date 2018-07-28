""" Tyrone de Ruiters
    3541544 """

""" Vernam encryption used to encrypt and decrypt a message or cipher.
    The ASCII value of each character in the message is added to the the corresponding ASCII value in the key."""

def encrypt(key, msg):
    ciph = []
    for i in range(len(msg)):
        ascii_sum = ord(msg[i]) + ord(key[i])
        ciph.append(chr(ascii_sum))
    return ciph

def decrypt(key, ciph):
    msg = []
    for i in range(len(ciph)):
        ascii_char = ord(ciph[i]) - ord(key[i])
        msg.append(chr(ascii_char))
    return msg

key = input("Insert key: ")
msg = input("Insert message/cipher: ")
if(len(key) != len(msg)):
    print("Error: lengths of key and message do not match.")
else:
    option = input("1. encrypt \n2. decrypt\n")
    if(option == "1"):
        print("encrypted message: " + "".join(encrypt(key, msg)))
    else:
        print("encrypted message: " + "".join(decrypt(key, msg)))

        
