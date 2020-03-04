##Author: Miguel Angel Alvarez Vargas (miguelangelalvarez3@gmail.com)
##Algorithm to cipher a message using Caesar's cipher. 

import sys

ABC="ABCDEFGHIJKLMNOPQRSTYVWXYZ"
abc="abcdefghijklmnopqrstuvwxyz"

if len(sys.argv) == 2:
    try:
        k = int(sys.argv[1])
    except:
        print("{} Can't be converted to int").format(sys.exc_info()[1])
        exit(1)
    message = raw_input("plaintext:").split()
    index = 0
    ciphertext = ""
    for word in message:
        for carac in message[index]:
            if carac in ABC:
                ciphertext += ABC[(ABC.index(carac)+k%(len(ABC)))-26]
            elif carac in abc:
                ciphertext += abc[(abc.index(carac)+k%(len(abc)))-26]
            else:
                ciphertext += carac
        ciphertext += " "
        index=index+1
    print("ciphertext: {}").format(ciphertext)
    print("\n")
else:
    print("Usage: python caesar.py k")
    exit(1)