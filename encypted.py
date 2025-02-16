import random
import string
chars=" "+ string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
print(f"chars : {chars}")

print(f"Key : {key}")

#encrypted
plain_text=input("Enter a massage to encryt : ")
cipher_text =''

for letter in plain_text :
    idex=chars.index(letter)
    cipher_text += key[idex]
    
print(f"Original massage : {plain_text}")
print(f"encrypted massage : {cipher_text}")
