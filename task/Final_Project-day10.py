def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mtply(n1, n2):
    return n1 * n2

def dvd(n1, n2):
    return n1 / n2

primul_numar = float(input("What is the first number?: "))
dictionar = {
    "+" : add,
    "-" : sub,
    "*" : mtply,
    "/" : dvd
}


for key in dictionar:
    print(key)

semn = input("Pick an operation: ")
second_number = float(input("What is the second number?: "))
rezultat = 0
rezultat = dictionar[semn](primul_numar,second_number)
print(f"{primul_numar} {semn} {second_number} = {rezultat}")

intrebare = input(f"Type 'y' if you want to continue calculating with {rezultat}, or 'n' to start another calculation.").lower()

if intrebare == "y":
    rezultat2 = 0
    while intrebare == 'y':

        for key in dictionar:
            print(key)

        semn = input("Pick an operation: ")
        second_number = float(input("What is the second number?: "))
        rezultat2 = dictionar[semn](rezultat,second_number)
        print(f"{rezultat} {semn} {second_number} = {rezultat2}")

        rezultat = rezultat2
        intrebare = input(f"Type 'y' if you want to continue calculating with {rezultat2}, or 'n' to start another calculation.").lower()
