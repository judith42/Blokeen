#Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.

uurloon = eval(input('Wat verdien je per uur: '))
gewerkteUren = eval(input('Hoeveel uur heb je gewerkt: '))

salaris =  (uurloon*gewerkteUren)

print (str(gewerkteUren) + ' uur werken levert ' + str(salaris)  + ' Euro op')

'''
Output: 
Wat verdien je per uur: 3.80
Hoeveel uur heb je gewerkt: 20
20 uur werken levert 76.0 Euro op
'''
