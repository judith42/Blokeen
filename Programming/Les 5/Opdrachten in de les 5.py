'''
naam = input('What is your naam: ')
leeftijd =  eval(input('Insert your age please: '))

if leeftijd < 18:
    print (naam + ' mag niet stemmen')
else:
    print (naam + ' je mag stemmen yay')
'''

'''
getallenlijst = [2, 4, 6, 8, 10, 9 ,7]
for getal in getallenlijst:
      print(getal)
woordenlijst = ['aap', 'noot', 'mies']
for woord in woordenlijst:
    print(woord)
   
'''

'''
woord = 'voorbeeld'
for letter in woord:
    print(letter)
'''

'''
getallenrij = [2, 4, 6, 8, 10, 9 ,7]
som = 0

for getal in getallenrij:
    som = som + getal
    print(getal)

print('dit is som' + str(som))
'''

'''
getallenrij = [2, 4, 6, 8, 10, 9, 7]
aantal = 0
for getal in getallenrij:
    if getal % 3 == 0:
        aantal += 1

print('het aantal getallen dat deelbaar is door 3' + str(aantal))
'''

'''
getallenrij = [2, 4, 6, 8, 10, 9, 7]

maximum = -1000

for getal in getallenrij:
    if getal > maximum:
        maximum = getal
print(maximum)
'''






