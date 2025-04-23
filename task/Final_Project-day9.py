user_name = input("What is your name?")
bid = int(input("What is your bid? $"))

info = {
    user_name: bid
}
question = input("Are there any other biders? Type 'yes'or 'no'").lower()

while question == "yes":
    info[user_name] = bid
    print("\n" * 100)
    user_name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    question = input("Are there any other biders? Type 'yes'or 'no'").lower()
    if question == "no":
        info[user_name] = bid
nume = ""
valoare = 0
for key in info:
    if info[key] > valoare:
        valoare = info[key]
        nume = key

print(f"The biggest bid was : {nume} - ${valoare}")