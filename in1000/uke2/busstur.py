# 2.11: Busstur

ant_plasser = 30
ant_passasjerer = 0
nye_passasjerer = 0
stasjon = 1

while stasjon <= 3:
    print(f'\nStasjon {stasjon}! Hvor mange gaar paa bussen?: ', end="")
    nye_passasjerer = int(input())
    ant_plasser -= nye_passasjerer
    ant_passasjerer += nye_passasjerer

    if ant_plasser <= 0:
        print(f'\nBussen er full. {abs(ant_plasser)} må gå til fots.')
        break
    elif ant_plasser > 0:
        print(f'\n{nye_passasjerer} nye passasjerer går ombord i bussen.')
        stasjon += 1

    if stasjon > 3:
        print(f'\nBussen er fremme med {ant_passasjerer} passasjerer ombord.')
