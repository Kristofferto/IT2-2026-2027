# IT2 1A - ØKT 1: utskrift, variabler, operatorer, biblioteker
# Oppgaver: 1-15
# Marker en seksjon og kjør med Shift+Enter.


# 1. Utskrift
print('Hei fra IT2!')
print('Svaret er', 42)
print('2026', '08', '31', sep='-')
print('-' * 30)


# 2. Variabler og datatyper
navn = 'Kari'
alder = 19
hoyde = 1.72

print(navn, alder, hoyde)
print(type(navn), type(alder), type(hoyde))

alder = alder + 1
print(alder)

print(int('42') + 1)
print(str(42) + ' år')
print(1 == 1)
print('Ola' == navn)

# 3. Operatorer
a = 7
b = 2

print(a + b, a - b, a * b)
print(a / b)  # 3.5  - alltid desimaltall
print(a // b)  # 3    - heltallsdivisjon
print(a % b)  # 1    - rest
print(a**b)  # 49   - potens

print(2 + 3 * 4)
print((2 + 3) * 4)


# 4. Operatorer på tekst
fornavn = 'Kari'
etternavn = 'Nordmann'

print(fornavn + ' ' + etternavn)
print('ha' * 3)
print('3' + '4')  # 34
print(3 + 4)  # 7


# 5. Biblioteker
import math  # heller numpy...

import numpy as np

print(np.pi)
print(math.sqrt(2))

import random

print(random.randint(1, 6))


# 6. Sjekk at pip install virket
# I terminalen:
#   python -m pip install numpy matplotlib

import matplotlib
import numpy

print(numpy.__version__)
print(matplotlib.__version__)
print('Alt klart!')
