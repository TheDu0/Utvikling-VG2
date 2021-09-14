
#Addering av to tall

import random


def addere():

    tall1 = int(input("Gi meg ett tall: "))
    tall2 = int(input("Gi meg enda ett tall: "))

    sum = tall1 + tall2 

    str(print("Summen av", tall1, "og", tall2, "er:", sum))
    starter()

#Multiplisering av to tall

def multiplisere():

    tall1 = int(input("Gi meg ett tall: "))
    tall2 = int(input("Gi meg enda ett tall: "))

    produkt = tall1 * tall2 

    str(print("Produktet av", tall1, "og", tall2, "er:", produkt))
    starter()

def terning():
    terning1 = 0
    terning2 = 0
    sum = 0

    while terning1 + terning2 !=12:
        input("Trykk på en tast")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        sum = terning1 + terning2
        print("Du fikk ", sum)

        if sum == 12:
            starter()

def starter():

    start = 0
    start = int(input("Velkommen til matte bot \n Skriv 1 for Addering \n Skriv 2 for Multiplisering \n Skriv 3 for terninger \n Skriv her: "))

    if start == 1:
        addere()

    elif start == 2:
        multiplisere()

    elif start == 3:
        terning()

    else:
        print("Du skrv inn feil tall")
starter()
