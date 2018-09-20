a = 6
b = 7
c = ((6+7)/2)
voornaam = 'Judtith'
tussenvoegsel =  ' '
achternaam = 'Boshoven'
mijnnaam = (voornaam+' '+ achternaam)

print((75 > a) and (75 < b)) #false
print((len(mijnnaam)) == (len(voornaam+achternaam))) #false
print((len(mijnnaam)*5)>(len(tussenvoegsel)))#true
print(tussenvoegsel in achternaam) #False

#test
print(len(mijnnaam))#16
print(len(voornaam+achternaam))