teRadenWoord = "Hogeschool"
weerTeGevenWoord = ""

for letter in teRadenWoord:
    if letter in ['a', 'e', 'o', 'u']:
        weerTeGevenWoord += '*'
    else:
        weerTeGevenWoord += '-'

print(weerTeGevenWoord)