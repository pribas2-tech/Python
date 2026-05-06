import random
random = random.randrange(1,10)
contadorIntents = 0
numInserit = 0



while random != numInserit:

    numInserit = int(input("Quin es el numero que he pensat?"))
    contadorIntents += 1

    if random < numInserit:
        print("El nummero es mes petit")
    elif random > numInserit:
        print("El numero es mes gran")
    if contadorIntents == 3:
        print(f"Has fet mes de tres intents! El nuemero era{random}")
        exit()

print(f"Perfecte! El numero era: {random}")



