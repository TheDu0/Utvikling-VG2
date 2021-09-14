import random

def fruktoggronnsak():
    frukt = "agurk"
    gronnsak = "eple"

    gronnsak = frukt 
    if gronnsak == "agurk":
        frukt = "eple"
    print(frukt, gronnsak)

def marte():

    navn="Marte"
    alder=22 
    if navn=="Maren" and alder==24:
        print("Du heter Maren og er 24år gammel")
    elif navn=="Maren" or alder==22:
        print("Du heter Maren eller er 22år")
    else:
        print("Du heter ikke Maren")

def tall1og2og3():
    tall1 = 14
    tall2 = 7
    tall3 = 11

    if tall1 > tall2:
        print(tall1, "er større enn", tall2)
    
    else:
        print(tall2, "er større enn", tall1)

    if tall1 > tall2 and tall1 > tall3:
        print(tall1, "er større enn", tall2, "og", tall3)
    
    elif tall1 < tall2 and tall2 < tall3:
        print(tall3, "er større enn", tall1, "og", tall2)
    
    elif tall1 < tall2 and tall2 > tall3:
        print(tall2, "er større enn", tall1, "og", tall3)

def jonatanogtobias():
    navnEn = "Jonatan"
    navnTo = "Tobias"

    if len(navnEn) > len(navnTo):
        print(navnEn, "har lenger navn enn", navnTo)
    
    else:
        print(navnTo, "har lenger navn enn", navnEn)

def foriogforu():
    for i in range(1,12):
        print(i)

    for u in range(11,0,-1):
        print(u)

def terning():
    terning = 0
    while terning !=571:
        
        terning = random.randint(1,999)
        print(terning)
    
    if terning == 571:
        print("Ferdig")

def bmi():
    alder = 0
    person = alder

    høyde = int(input("Hei og Velkommen Til BMI Kalkulatoren \n Skriv inn høyden din her(cm): "))
    vekt = int(input("Nå skriv inn vekten din(kg): "))

    høydeM = høyde / 100

    kmi = vekt / høydeM*høydeM
    print(kmi)
