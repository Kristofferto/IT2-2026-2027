# IT2 1A - ØKT 2: tekster, input, feil, formatering
# Oppgaver: 16-23
# Marker en seksjon og kjør med Shift+Enter.


# 1. Tekster

tekst = 'datamaskin'

print(len(tekst))
print('maskin' in tekst)
print(tekst.upper())
print(tekst.replace('data', 'vaske'))
print('  hei  '.strip())  # fjerner tomrom før og etter ord
setning = 'dette,er,jo,egentlig,ganske,spennede'
# lager en ny liste med substringene basert på hvilket tegn som separerer de
print(setning.split(','))


# 2. Indeksering

#     d    a    t    a    m    a    s    k    i    n
#     0    1    2    3    4    5    6    7    8    9
#   -10   -9   -8   -7   -6   -5   -4   -3   -2   -1

print(tekst[0])
print(tekst[4])
print(tekst[-1])
# print(tekst[10])     -> IndexError


# 3. Utsnitt

print(tekst[0:4])  # data   - til, men ikke med, 4
print(tekst[4:])  # maskin
print(tekst[:4])  # data
print(tekst[::-1])  # baklengs


# 4. Input fra bruker

navn = input('Hva heter du? ')
print('Hei,', navn)
print('Første bokstav:', navn[0])

alder = int(input('Alder? '))  # int() er nødvendig
print(alder + 10)

# input() gir ALLTID tekst.
#   alder = input(...)  ->  "19" + 1  ->  TypeError


# 5. Feil og feilmeldinger

# Les NEDERSTE linje i feilmeldingen først. Så linjenummeret.
# Fjern # foran én linje av gangen:

# print('Hei)
# print(tekst + 5)
# print(int('tre'))
# print(tekst[20])
# print(10 / 0)

# Feilsøking: skriv ut verdien og typen
pris = '249'
print(pris, type(pris))
print(pris * 3)  # 249249249  - logisk feil
print(int(pris) * 3)  # 747


# 6. Formatering

pris = 21.9
antall = 3

print('Sum: ' + str(antall * pris))  # 65.69999999999999
print(f'Sum: {antall * pris:.2f} kr')  # 65.70

alder = 19
print(f'Kari er {alder} år, og blir {alder + 10}.')


# 7. Justering

tall = 3.14159

print(f'[{"Vare":<12}]')  # venstre
print(f'[{"Vare":>12}]')  # høyre
print(f'[{"Vare":^12}]')  # midtstilt
print(f'[{tall:>12.2f}]')


# 8. Ryddig tabell

print(f'{"Vare":<12}{"Antall":>8}{"Pris":>10}')
print('-' * 30)
print(f'{"Melk":<12}{2:>8}{21.90:>10.2f}')
print(f'{"Kaffe":<12}{3:>8}{89.00:>10.2f}')


# 9. Spesialtegn

print('Første\nAndre')
print('Navn:\tKari')
print('Hun sa "hei".')
