import random

character = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

longitud = int(input("introducir longitud de la contraseña"))

password = ""   

for i in range(longitud):
    password += random.choice(character)

print(password)
