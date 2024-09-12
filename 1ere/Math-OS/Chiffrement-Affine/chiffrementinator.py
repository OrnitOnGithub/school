alphabet = "ABCDEFGHIJKLMNOPQRSTUVWKYZ"


# f(x) = ax + b pour chaque char.
def code(a, b, message):
    message_codé = ""

    for char in message:
        char_num = alphabet.index(char)
        message_codé += alphabet[(a * char_num + b) % 26]

    return message_codé


print(code(11, 8, "JOUR"))


# trouve la fonction reciproque, apelle `code` avec
def decode(a, b, message):
    for i in range(1, 26):
        if (a*i)%26 == 1:
            c = i
            d = -i *b

    return code(c, d, message)



def decode2(a, b, message):
    for i in range(1,26):
        if (a*i)%26==1:
            c = i
            d = -i * b

    return code(c, d, message)

print(decode(11, 8, "DGUN"))