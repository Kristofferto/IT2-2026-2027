"""
IT2 - REPETISJON
Tester

Slik bruker du fila:
  1. Lagre dine egne funksjoner i en fil som heter mine_svar.py
     i samme mappe som denne.
  2. Kjør denne fila.

Du får OK, FEIL eller IKKE LAGET for hver oppgave.
Oppgaver du ikke har gjort ennå stopper ikke testingen.

Oppgave 12 og 13 leser fra bruker og testes ikke her.
"""

import importlib

MODUL = 'mine_svar'

try:
    svar = importlib.import_module(MODUL)
except ModuleNotFoundError:
    print(f'Fant ikke {MODUL}.py. Lagre funksjonene dine i den fila først.')
    raise SystemExit

antall_ok = 0
antall_feil = 0
antall_mangler = 0


def meld(nummer, navn, status, melding=''):
    print(f'{nummer:>3}. {navn:<22}{status:<12}{melding}')


# 1. badminton
try:
    assert svar.badminton(True, True, False)
    assert not svar.badminton(True, True, True)
    assert not svar.badminton(False, False, False)
    assert svar.badminton(False, True, True)
    meld(1, 'badminton', 'OK')
    antall_ok += 1
except AttributeError:
    meld(1, 'badminton', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(1, 'badminton', 'FEIL')
    antall_feil += 1

# 2. poeng
try:
    assert svar.poeng('hjerte') == 6
    assert svar.poeng('lyn') == 0
    assert svar.poeng('firkløver') == 9
    assert svar.poeng('lyspære') == 7
    meld(2, 'poeng', 'OK')
    antall_ok += 1
except AttributeError:
    meld(2, 'poeng', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(2, 'poeng', 'FEIL')
    antall_feil += 1

# 3. jages
try:
    assert svar.jages(['mus', 'katt'])
    assert not svar.jages(['mus', 'mus', 'hund'])
    assert svar.jages(['hund', 'katt'])
    assert not svar.jages(['hund', 'hund'])
    assert not svar.jages([])
    meld(3, 'jages', 'OK')
    antall_ok += 1
except AttributeError:
    meld(3, 'jages', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(3, 'jages', 'FEIL')
    antall_feil += 1

# 4. poengsum
try:
    assert svar.poengsum(['hjerte', 'lyspære']) == 13
    assert svar.poengsum(['lyn', 'lyn']) == 0
    assert svar.poengsum([]) == 0
    meld(4, 'poengsum', 'OK')
    antall_ok += 1
except AttributeError:
    meld(4, 'poengsum', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(4, 'poengsum', 'FEIL')
    antall_feil += 1

# 5. bordsetting
try:
    assert svar.bordsetting(['Per', 'Palle'], ['Kari', 'Mia']) == [
        'Per',
        'Kari',
        'Palle',
        'Mia',
    ]
    assert svar.bordsetting(['A'], ['B']) == ['A', 'B']
    assert svar.bordsetting([], []) == []
    meld(5, 'bordsetting', 'OK')
    antall_ok += 1
except AttributeError:
    meld(5, 'bordsetting', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(5, 'bordsetting', 'FEIL')
    antall_feil += 1

# 6. felles
try:
    assert sorted(svar.felles([[1, 5, 1], [3, 4], [2, 3]])) == [1, 3]
    assert sorted(svar.felles([[1, 2], [3, 4]])) == []
    assert sorted(svar.felles([[7, 7, 7]])) == [7]
    meld(6, 'felles', 'OK')
    antall_ok += 1
except AttributeError:
    meld(6, 'felles', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(6, 'felles', 'FEIL', 'husk at hvert tall bare skal med én gang')
    antall_feil += 1

# 7. adskilt
try:
    assert svar.adskilt([[1, 10], [6, 8], [2, 3]])
    assert not svar.adskilt([[1, 10], [6, 8], [2, 3, 7]])
    assert svar.adskilt([[1, 2], [5, 6]])
    assert not svar.adskilt([[1, 5], [3, 9]])
    meld(7, 'adskilt', 'OK')
    antall_ok += 1
except AttributeError:
    meld(7, 'adskilt', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(7, 'adskilt', 'FEIL', 'sammenlign ikke en liste med seg selv')
    antall_feil += 1

# 8. heie
try:
    assert svar.heie({'Rosenborg': 4, 'Odd': 1, 'Molde': 3, 'Brann': 2}) == 'Brann'
    assert svar.heie({'Rosenborg': 2, 'Odd': 1, 'Molde': 3, 'Brann': 4}) == 'Odd'
    assert svar.heie({'Odd': 3, 'Brann': 1}) == 'Brann'
    assert svar.heie({'Odd': 1, 'Brann': 3}) == 'Brann'
    meld(8, 'heie', 'OK')
    antall_ok += 1
except AttributeError:
    meld(8, 'heie', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(8, 'heie', 'FEIL', 'plass 3 teller som bra nok')
    antall_feil += 1

# 9. flertall
try:
    assert svar.flertall(['ulv', 'sau', 'ulv']) == 'ulv'
    assert svar.flertall(['ulv', 'sau', 'sau', 'ulv']) == 'uavgjort'
    assert svar.flertall(['sau']) == 'sau'
    assert svar.flertall(['a', 'a', 'b', 'c']) == 'a'
    meld(9, 'flertall', 'OK')
    antall_ok += 1
except AttributeError:
    meld(9, 'flertall', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(9, 'flertall', 'FEIL')
    antall_feil += 1

# 10. utvidet_jages
try:
    assert svar.utvidet_jages(['ulv', 'mus', 'sau'], {'ulv': 'sau'})
    assert not svar.utvidet_jages(['ulv', 'mus', 'hund'], {'ulv': 'sau', 'katt': 'mus'})
    assert not svar.utvidet_jages(['sau'], {'ulv': 'sau'})
    assert svar.utvidet_jages(['katt', 'mus'], {'ulv': 'sau', 'katt': 'mus'})
    meld(10, 'utvidet_jages', 'OK')
    antall_ok += 1
except AttributeError:
    meld(10, 'utvidet_jages', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(10, 'utvidet_jages', 'FEIL', 'både jeger og bytte må være i lista')
    antall_feil += 1

# 11. lag_interessegrupper
try:
    assert svar.lag_interessegrupper(
        {'Per': 'Mat', 'Palle': 'Film', 'Espen': 'Mat'}
    ) == {
        'Mat': ['Per', 'Espen'],
        'Film': ['Palle'],
    }
    assert svar.lag_interessegrupper({}) == {}
    assert svar.lag_interessegrupper({'A': 'X'}) == {'X': ['A']}
    meld(11, 'lag_interessegrupper', 'OK')
    antall_ok += 1
except AttributeError:
    meld(11, 'lag_interessegrupper', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(11, 'lag_interessegrupper', 'FEIL')
    antall_feil += 1

# 14. stigespill
try:
    assert svar.stigespill([5, 4, 2, 2], {5: 12, 18: 7}) == 9
    assert svar.stigespill([], {5: 12}) == 0
    assert svar.stigespill([3], {}) == 3
    assert svar.stigespill([3, 3], {3: 20}) == 23
    meld(14, 'stigespill', 'OK')
    antall_ok += 1
except AttributeError:
    meld(14, 'stigespill', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(14, 'stigespill', 'FEIL', 'sjekk stigen etter HVERT kast')
    antall_feil += 1

# 15. hvilke_tre_kast
try:
    fasit = [[1, 1, 3], [1, 3, 1], [2, 2, 1], [3, 2, 1]]
    assert sorted(svar.hvilke_tre_kast(5, {3: 15, 17: 4})) == fasit
    assert svar.hvilke_tre_kast(100, {}) == []
    assert sorted(svar.hvilke_tre_kast(3, {})) == [[1, 1, 1]]
    meld(15, 'hvilke_tre_kast', 'OK')
    antall_ok += 1
except AttributeError:
    meld(15, 'hvilke_tre_kast', 'IKKE LAGET')
    antall_mangler += 1
except AssertionError:
    meld(15, 'hvilke_tre_kast', 'FEIL', 'terningen går fra 1 til 6')
    antall_feil += 1

print()
print(f'OK: {antall_ok}   Feil: {antall_feil}   Ikke laget: {antall_mangler}')
print('Oppgave 12, 13 og 16 testes ikke - de leser fra bruker eller skriver ut.')
