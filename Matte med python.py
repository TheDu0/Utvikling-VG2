høyde = int(input("Skriv inn høyde: "))
bredde = int(input("Skriv inn bredde: "))

areal = høyde*bredde
omkrets = 2*bredde + 2*høyde
print("Arealet til objektet er: " + str(areal))
print("Omkretsen er: " + str(omkrets))

#regner ut areal og omkrets av en trekant

høyde = int(input("Skriv inn høyden til trekanten: "))
grunnlinje = int(input("Skriv inn bredden: "))

areal = høyde*grunnlinje/2
print("Arealet til trekant er: " + str(areal))