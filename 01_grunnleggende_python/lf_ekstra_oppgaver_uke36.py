"""
IT2 1A - UTFORDRINGER, LØSNINGSFORSLAG

Testverdiene er skrevet rett inn så fila kan kjøres i sin helhet.
input()-linja står som kommentar der den hører hjemme.
"""

import math

"""
1. KLOKKA
"""

sekunder = 78125  # input('Antall sekunder: ')

timer = sekunder // 3600
minutter = sekunder % 3600 // 60
sek = sekunder % 60

print(f'{timer:02d}:{minutter:02d}:{sek:02d}')

# c) klokkeslett på et døgn
sekunder = 100000
print(f'{sekunder // 3600 % 24:02d}:{sekunder % 3600 // 60:02d}:{sekunder % 60:02d}')


"""
2. SIFFERSUM
"""

tall = 48219  # input('Femsifret tall: ')

# a) med // og %
sum_a = (
    tall // 10000 + tall // 1000 % 10 + tall // 100 % 10 + tall // 10 % 10 + tall % 10
)
print(f'Siffersum: {sum_a}')

# b) uten // og %
t = str(tall)
sum_b = int(t[0]) + int(t[1]) + int(t[2]) + int(t[3]) + int(t[4])
print(f'Siffersum: {sum_b}')

# c) Variant b er lettest å lese. Variant a virker derimot for tall av
#    alle lengder når du senere lærer løkker.


"""
3. PALINDROM
"""

tekst = 'Regninger'  # input('Skriv et ord: ')
tekst = tekst.lower()  # d) uten denne feiler stor forbokstav

print(f'Baklengs: {tekst[::-1]}')
print(f'Palindrom: {tekst == tekst[::-1]}')

# Sammenligningen gir True eller False helt av seg selv.
# Derfor trengs ingen if.

print(f'agnes er palindrom: {"agnes" == "agnes"[::-1]}')


"""
4. TALLSYSTEMER
"""

print(f'{255:b}  {255:o}  {255:x}')
print(f'Tilbake igjen: {int("11111111", 2)}')

print(f'1000 trenger {len(f"{1000:b}")} bits')
print(f'Største tall i 8 bits:  {2**8 - 1}')
print(f'Største tall i 16 bits: {2**16 - 1}')


"""
5. DET UMULIGE REGNESTYKKET
"""

print(f'{0.1 + 0.2 == 0.3}')
print(f'{0.1 + 0.2:.20f}')
print(f'isclose: {math.isclose(0.1 + 0.2, 0.3)}')

# b) 0,1 kan ikke skrives eksakt i totallsystemet, like lite som 1/3 kan
#    skrives eksakt med desimaler. Avviket er bittelite, men det er der.
# c) == krever eksakt likhet. isclose spør om tallene er nær nok.
#    Nesten all sammenligning av desimaltall bør gjøres på den måten.
# d) 0.1 + 0.7 er også unøyaktig. 0.5 + 0.25 er derimot eksakt,
#    fordi begge er potenser av 1/2 og går opp i totallsystemet.

print(f'{0.5 + 0.25 == 0.75}')


"""
6. RAMME
"""

navn = 'Kari'  # input('Skriv et ord: ')
bredde = len(navn) + 4

print(f'{"*" * bredde}')
print(f'*{navn:^{bredde - 2}}*')
print(f'{"*" * bredde}')


"""
7. HEMMELIG KODE
"""

bokstav = 'y'  # input('Én liten bokstav: ')

# a) uten omvikling - feiler på x, y, z
print(f'{chr(ord(bokstav) + 3)}')

# b) med omvikling. Vi trekker fra 97 for å komme ned til 0-25,
#    regner rundt med % 26, og legger 97 på igjen.
print(f'{chr((ord(bokstav) - 97 + 3) % 26 + 97)}')

# c) tre bokstaver
o = 'hei'
kodet = (
    chr((ord(o[0]) - 97 + 3) % 26 + 97)
    + chr((ord(o[1]) - 97 + 3) % 26 + 97)
    + chr((ord(o[2]) - 97 + 3) % 26 + 97)
)
print(f'{o} kodes til {kodet}')

# d) dekoding: bytt + 3 med - 3. % 26 ordner resten.
klart = (
    chr((ord(kodet[0]) - 97 - 3) % 26 + 97)
    + chr((ord(kodet[1]) - 97 - 3) % 26 + 97)
    + chr((ord(kodet[2]) - 97 - 3) % 26 + 97)
)
print(f'{kodet} dekodes til {klart}')


"""
8. KVITTERINGEN
"""

vare1, ant1, pris1 = 'Melk', 2, 21.90
vare2, ant2, pris2 = 'Kaffefilter', 1, 34.50
vare3, ant3, pris3 = 'Brød', 3, 89.00

bredde = max(len(vare1), len(vare2), len(vare3)) + 2

sum1 = ant1 * pris1
sum2 = ant2 * pris2
sum3 = ant3 * pris3
sum_eks = sum1 + sum2 + sum3
mva = sum_eks * 0.25

print(f'{"Vare":<{bredde}}{"Ant":>5}{"Pris":>10}{"Sum":>10}')
print(f'{"-" * (bredde + 25)}')
print(f'{vare1:<{bredde}}{ant1:>5}{pris1:>10.2f}{sum1:>10.2f}')
print(f'{vare2:<{bredde}}{ant2:>5}{pris2:>10.2f}{sum2:>10.2f}')
print(f'{vare3:<{bredde}}{ant3:>5}{pris3:>10.2f}{sum3:>10.2f}')
print(f'{"-" * (bredde + 25)}')
print(f'{"Sum eks. mva":<{bredde}}{"":>5}{"":>10}{sum_eks:>10.2f}')
print(f'{"Mva 25%":<{bredde}}{"":>5}{"":>10}{mva:>10.2f}')
print(f'{"Totalt":<{bredde}}{"":>5}{"":>10}{sum_eks + mva:>10.2f}')
