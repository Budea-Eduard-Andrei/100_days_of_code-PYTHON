import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#lista = [letters+numbers+symbols]
#aux = nr_numbers+nr_symbols+nr_letters
# for aux in range(1,nr_letters + 1):
#     for aux1 in range(1, nr_symbols + 1):
#         for aux2 in range(1, nr_numbers + 1):
#             parola = parola + random.choice(letters)
#             parola = parola + random.choice(symbols)
#             parola = parola + random.choice(numbers)
#for aux1 in range(1, aux + 1):
lista = []
parola = ""
for aux in range(1, nr_letters + 1):
    parola += random.choice(letters)

for aux in range(1, nr_symbols + 1):
    parola += random.choice(symbols)

for aux in range(1, nr_numbers + 1):
    parola += random.choice(numbers)

for aux in range(0, len(parola)):
    lista.append(parola[aux])
random.shuffle(lista)
parola = ""
for char in lista:
    parola += char

print(parola)



