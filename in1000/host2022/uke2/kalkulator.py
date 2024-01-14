# 02.17: Kalkulator

def kalkulator():
    tall1 = float(input("Skriv inn tall 1: "))
    operasjon = input("Skriv inn en operasjon (+, -, *, /): ")
    tall2= float(input("Skriv inn tall 2: "))
    
    sum = 0

    if operasjon == "+":
        sum = tall1+tall2
        print("Summen er: ", sum)
    
    elif operasjon == "-":
        sum = tall1-tall2
        print("Summen er: ", sum)
    elif operasjon == "*":
        sum = tall1*tall2
        print("Produktet er: ", sum)
    elif operasjon == "/":
        sum = tall1/tall2
        print("Kvotienten er: ", sum)
    else:
        print("Ugyldig operasjon!")
    
kalkulator()