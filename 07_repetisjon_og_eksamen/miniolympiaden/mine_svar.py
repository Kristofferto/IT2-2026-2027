"""
IT2 - IT-OLYMPIADEN, LØSNINGSFORSLAG
"""

"""
1. SAMME SOPP
"""


def samme_sopp(per_sopp, kari_sopp, nils_sopp):
    return per_sopp == kari_sopp or per_sopp == nils_sopp or kari_sopp == nils_sopp


"""
2. TELL GIFTIGE
"""


def tell_giftige(giftige, plukket):
    teller = 0
    for sopp in plukket:
        if sopp in giftige:
            teller += 1
    return teller


"""
3. FINN TRYGG SOPP
"""


def finn_trygg_sopp(giftige, plukket):
    for sopp in plukket:
        if sopp not in giftige:
            return sopp  # stopper på den første
    return None


"""
4. JAGES
"""


def jages(dyreliste):
    for jeger in dyreliste:
        for bytte in dyreliste:
            if jeger == 'hund' and bytte == 'katt':
                return True
            if jeger == 'katt' and bytte == 'mus':
                return True
    return False


"""
5. FLERTALL
"""


def flertall(dyreliste):
    telling = {}
    for dyr in dyreliste:
        if dyr in telling:
            telling[dyr] += 1
        else:
            telling[dyr] = 1

    beste = ''
    flest = 0
    uavgjort = False

    for dyr, antall in telling.items():
        if antall > flest:
            beste = dyr
            flest = antall
            uavgjort = False
        elif antall == flest:
            uavgjort = True

    if uavgjort:
        return 'uavgjort'
    return beste


"""
6. KATEGORISER SOPPER
"""


def kategoriser_sopper(kategorier, plukket):
    svar = {}
    for kategori, sopper in kategorier.items():
        antall = tell_giftige(sopper, plukket)  # gjenbruk fra oppgave 2
        if antall > 0:
            svar[kategori] = antall
    return svar


"""
7. STIGESPILLET
"""


def stigespill(terningkast, stiger):
    posisjon = 0
    for kast in terningkast:
        posisjon += kast
        if posisjon in stiger:
            posisjon = stiger[posisjon]
    return posisjon


"""
8. FINN SOPP
"""


def finn_sopp(egenskaper1, egenskaper2, soppguide):
    treff = 0
    indre = None

    for nokkel in soppguide:
        if nokkel in egenskaper1:
            treff += 1
            indre = soppguide[nokkel]

    if treff != 1:
        return 'uklar'

    treff = 0
    soppnavn = None

    for nokkel in indre:
        if nokkel in egenskaper2:
            treff += 1
            soppnavn = indre[nokkel]

    if treff != 1:
        return 'uklar'

    return soppnavn


"""
9. IDENTIFISER SOPP
"""


def neste_nivå(liste, ordbok):
    teller = 0
    # verdi = None
    for element in liste:
        if element in ordbok:
            teller += 1
            verdi = ordbok[element]
    if teller != 1:
        return 'uklar'
    return verdi


def identifiser_sopp(egenskaper, soppguide):
    verdi = neste_nivå(egenskaper, soppguide)
    while type(verdi) == dict:
        verdi = neste_nivå(egenskaper, verdi)
    return verdi


# Nøkkelen i oppgave 9 er at vi ikke vet hvor dypt det går.
# Derfor en while-løkke som flytter seg nedover, i stedet for
# to omganger som i oppgave 8.
