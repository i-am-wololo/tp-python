import struct

with open("testfile") as file:
    print("afficher les 12 premiers caracteres avec 2 read()")
    print("-"*10)
    print(file.read(6))
    print(file.read(6))
    print()

with open("testfile") as file:
    print("-"*10)
    print("afficher premiere et troisieme ligne")


