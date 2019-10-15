# 2.11: Busstur

ant_plasser = 30
ant_passasjerer = 0
nye_passasjerer = 0
stasjon = 1
temp = 0

while stasjon <= 3:
    print(f'Stasjon {stasjon}! Hvor mange gaar paa bussen?: ', end="")
    nye_passasjerer = int(input())
    ant_passasjerer = ant_passasjerer + nye_passasjerer

    if ant_passasjerer > 30:
        ant_plasser = ant_plasser - ant_passasjerer
        print(f'Bussen er full. {} må gå.')
        break
    else:
        ant_passasjerer = ant_passasjerer + nye_passasjerer
        ant_plasser = (ant_plasser - ant_passasjerer)
        stasjon = stasjon+1
