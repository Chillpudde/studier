# Oppgave 3: Problemløsning med beslutninger

"""
ABOUT
-------------
Programmet tar IKKE hensyn til om man skriver inn en dato som ikke finnes.
Det kreves av bruker at dato skrives inn nøyaktig etter formatet (DDMM) for
at progammet skal gi et fornuftig resultat.
For "optimal" funksjon burde følgende fikses:
- Ta hensyn til år
- Sjekke at formatet stemmer
- La bruker skrive inn et "skillesymbol" (ex. DD.MM.YY)
- Og div annet... holdt meg til oppgavens "scope"
"""
print("\n")
print("| Skriv inn to datoer i kronologisk rekkefolge |\n")

dato_1 = int(input("Skriv inn forste dato (DDMM): "))
dato_2 = int(input("Skriv inn andre dato (DDMM): "))

# Runder opp ved å bruke "int" (finnes mer elegante måter å gjøre det på...)
dag_1 = (int(dato_1/100))
dag_2 = (int(dato_2/100))

# Bruker "%" operator for å hente ut tallene fra tusen- og hundredelsplassen
mnd_1 = (dato_1%100)
mnd_2 = (dato_2%100)

"""
I oppgaveteksten står det: ...sikre at sammenligningen i programmet ditt
kan gjøres enklere... Usikker på hvordan jeg skal
gjøre sammenlikningen meningsfullt "enklere", gitt de verktøyene pensumet har
dekket frem til nå...
"""

if (dag_1 < dag_2 and mnd_1 <= mnd_2) or (dag_1 >= dag_2 and mnd_1 < mnd_2):
    print("Riktig rekkefolge!")
elif (mnd_1 > mnd_2) or (mnd_1 == mnd_2 and dag_1 > dag_2):
    print("Feil rekkefolge!")
else:
    print("Samme dato!")
