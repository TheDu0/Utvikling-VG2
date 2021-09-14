import random

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


def telle():
    for i in range(70):
        print(i)
        if i == 70/2:
            print("Du er halvveis")

def frukt():
    frukt = ["Epple", "Pære", "Sitron"]

    frukt.append("Plomme")

    nfrukt = input("Skriv frukt: ")
    frukt.append(nfrukt)
    print(frukt)

def klasselist():
    klasseliste = []
    elev = ''
    while elev !="stopp":
        elev = input("Skriv inn navn: ")
        klasseliste.append(elev)
        if elev == "stopp":
            klasseliste.remove("stopp")
        elif elev == "Stopp":
            klasseliste.remove("Stopp")
            
        print(klasseliste)

klasselist()
