# IT2 - funksjoner
# Krever at minmatte.py ligger i samme mappe.

import minmatte
import numpy as np

# 1. Introduksjon


def hils():
    print('Hei!')


hils()
hils()

# def lager funksjonen. Ingenting skjer før du kaller den.
# Alt som er innrykket hører til funksjonen.


# 2. Funksjoner med parametre


def areal(bredde, hoyde):
    return bredde * hoyde


print(areal(3, 4))
print(areal(hoyde=4, bredde=3))  # navngitte argumenter, rekkefølgen er fri


def pris_med_mva(pris, sats=0.25):
    return pris * (1 + sats)


print(pris_med_mva(100))
print(pris_med_mva(100, 0.15))

# Parametre med standardverdi må stå sist.


# 3. Returverdier


def dobbel(tall):
    return tall * 2


print(dobbel(5) + dobbel(3))  # du kan regne videre med svaret


def dobbel_feil(tall):
    print(tall * 2)


print(dobbel_feil(21))  # None - funksjonen returnerte ingenting


def fraktpris(vekt):
    if vekt < 1:
        return 49  # return avslutter funksjonen med én gang
    if vekt <= 5:
        return 89
    return 149


print(fraktpris(0.5), fraktpris(3), fraktpris(12))


def min_og_maks(liste):
    minst = liste[0]
    storst = liste[0]
    for verdi in liste:
        if verdi < minst:
            minst = verdi
        if verdi > storst:
            storst = verdi
    return minst, storst


lav, hoy = min_og_maks([12, 4, 19, 7])
print(lav, hoy)

samlet = min_og_maks([12, 4, 19, 7])
print(samlet)  # uten oppdeling får du en tuppel


# 4. Variabler og rekkevidde


def regn_ut():
    hjelp = 10  # lokal variabel
    return hjelp * 2


print(regn_ut())
# print(hjelp)   -> NameError. Finnes bare inne i funksjonen.

antall = 5


def les_antall():
    return antall  # globale variabler kan LESES


def endre_antall():
    antall = 99  # lager en NY lokal variabel, rører ikke den globale


print(les_antall())
endre_antall()
print(antall)

# Tall sendes som kopi. Lister og ordbøker sendes som seg selv:


def legg_til_null(liste):
    liste.append(0)


tall = [1, 2, 3]
legg_til_null(tall)
print(tall)  # originalen ble endret


def legg_til_en(verdi):
    verdi += 1


x = 5
legg_til_en(x)
print(x)  # uendret

# Vil du beskytte originalen: send inn liste.copy()


# 5. Dokumentasjon


def omkrets(radius):
    """Returnerer omkretsen av en sirkel med gitt radius."""
    return 2 * np.pi * radius


print(omkrets.__doc__)
print(f'{omkrets(4):.2f}')

# Docstring er tre anførselstegn rett under def.
# Hold musepekeren over navnet i VS Code, så dukker den opp.


# 6. Egne biblioteker

# minmatte.py er en helt vanlig Python-fil med funksjoner i.
# import minmatte gjør dem tilgjengelige her.

tall = [12.4, 8.1, 15.7, 3.2]

print(minmatte.summer(tall))
print(minmatte.snitt(tall))
print(minmatte.storste(tall))

# Alternativ form, da slipper du å skrive minmatte foran:
from minmatte import minste

print(minste(tall))

# Testkoden nederst i minmatte.py kjørte ikke.
# Den står bak if __name__ == '__main__':
