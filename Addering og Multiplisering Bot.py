
#Addering av to tall

def addere():

    tall1 = int(input("Gi meg ett tall: "))
    tall2 = int(input("Gi meg enda ett tall: "))

    sum = tall1 + tall2 

    str(print("Summen av", tall1, "og", tall2, "er:", sum))

#Multiplisering av to tall

def multiplisere():

    tall1 = int(input("Gi meg ett tall: "))
    tall2 = int(input("Gi meg enda ett tall: "))

    produkt = tall1 * tall2 

    str(print("Produktet av", tall1, "og", tall2, "er:", produkt))


start = 0
start = int(input("Velkommen til matte bot \n Skriv 1 for Addering \n Skriv 2 for Multiplisering \n Skriv her: "))

if start == 1:
    addere()

elif start == 2:
    multiplisere()

else:
    print("Du skrv inn feil tall")

