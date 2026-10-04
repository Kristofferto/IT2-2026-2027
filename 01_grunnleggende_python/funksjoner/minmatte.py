"""Egne funksjoner til IT2. Importeres med: import minmatte"""


def summer(liste):
    """Returnerer summen av tallene i liste."""
    sum_tall = 0
    for verdi in liste:
        sum_tall += verdi
    return sum_tall


def snitt(liste):
    """Returnerer gjennomsnittet av tallene i liste."""
    return summer(liste) / len(liste)


def storste(liste):
    """Returnerer den største verdien i liste."""
    beste = liste[0]
    for verdi in liste:
        if verdi > beste:
            beste = verdi
    return beste


def minste(liste):
    """Returnerer den minste verdien i liste."""
    beste = liste[0]
    for verdi in liste:
        if verdi < beste:
            beste = verdi
    return beste


# Kjører bare når fila startes direkte, ikke når den importeres.
if __name__ == '__main__':
    test = [4, 9, 2, 7]
    print(summer(test), snitt(test), storste(test), minste(test))
