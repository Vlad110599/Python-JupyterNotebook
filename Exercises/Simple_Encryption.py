#Simple Encryption
import string

text = "This is a text! Hello World!"
shift = 7

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet,shifted)

encrypted = text.translate(table)

print(encrypted)