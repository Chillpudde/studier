# 2.14: Tekstformatering med utskrift

width = 0
list = ["Arne", "Dag", "Ellen"]

n = 0
for i in list:
    if len(list[n]) > width:
        width = len(list[n])
    n +=1

count = 0

for i in list:
    count +=1
    print('Navn', count, end='')
    print(':', i.rjust(width,' '))
