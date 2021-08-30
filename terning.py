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



for i in range(70):
    print(i)
    if i == 35:
        print("yeeey")
    