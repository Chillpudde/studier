# 02.20: Busstur

plasser = 30
passasjerer = 0 #maks 30, kan ikke overstige antall plasser
nye_passasjerer = 0
stasjon_nummer = 1

nye_passasjerer = int(input("Stasjon {}! Hvor mange gaar paa bussen?: ".format(stasjon_nummer)))
if (nye_passasjerer <= plasser):
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    stasjon_nummer += 1
    print(nye_passasjerer, "gaar ombord.")
else:
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    print("Bussen er full!", passasjerer-30, "maa gaa til fots.")
    quit()

nye_passasjerer = int(input("Stasjon {}! Hvor mange gaar paa bussen?: ".format(stasjon_nummer)))
if (nye_passasjerer <= plasser):
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    stasjon_nummer += 1
    print(nye_passasjerer, "gaar ombord.")
else:
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    print("Bussen er full!", passasjerer-30, "maa gaa til fots.")
    quit()

nye_passasjerer = int(input("Stasjon {}! Hvor mange gaar paa bussen?: ".format(stasjon_nummer)))
if (nye_passasjerer <= plasser):
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    stasjon_nummer += 1
    print(nye_passasjerer, "gaar ombord.")
else:
    passasjerer += nye_passasjerer
    plasser -= passasjerer
    print("Bussen er full!", passasjerer-30, "maa gaa til fots.")

print("Bussen kjorer til endestasjonen med", passasjerer, "passasjerer.")
