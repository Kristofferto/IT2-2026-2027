"""
IT2 - IT-OLYMPIADEN
Tester

Lagre funksjonene i mine_svar.py i samme mappe, og kjør denne fila.

Testene er de samme som står i oppgaveteksten. Oppgavene testes i
rekkefølge, og dere kommer ikke videre før den dere står på er grønn.

Når en oppgave blir godkjent får dere en kode. Skriv den inn på
løpsbanen for å flytte hesten deres fram til neste post.
"""

import importlib

MODUL = 'mine_svar'

try:
    svar = importlib.import_module(MODUL)
except ModuleNotFoundError:
    print(f'Fant ikke {MODUL}.py. Lag fila først.')
    raise SystemExit


def test_1():
    assert svar.samme_sopp('kantarell', 'fluesopp', 'kantarell') == True
    assert svar.samme_sopp('kantarell', 'fluesopp', 'steinsopp') == False


def test_2():
    assert (
        svar.tell_giftige(
            ['fluesopp', 'hvit fluesopp'], ['kantarell', 'fluesopp', 'steinsopp']
        )
        == 1
    )
    assert svar.tell_giftige(['fluesopp'], ['fluesopp', 'fluesopp', 'kantarell']) == 2


def test_3():
    assert (
        svar.finn_trygg_sopp(['fluesopp'], ['fluesopp', 'kantarell', 'steinsopp'])
        == 'kantarell'
    )
    assert (
        svar.finn_trygg_sopp(['fluesopp', 'kantarell'], ['fluesopp', 'kantarell'])
        == None
    )


def test_4():
    assert svar.jages(['mus', 'katt']) == True
    assert svar.jages(['mus', 'mus', 'hund']) == False


def test_5():
    assert svar.flertall(['ulv', 'sau', 'ulv']) == 'ulv'
    assert svar.flertall(['ulv', 'sau', 'sau', 'ulv']) == 'uavgjort'


def test_6():
    assert svar.kategoriser_sopper(
        {
            'giftige': ['fluesopp', 'spiss giftslørsopp'],
            'matsopper': ['kantarell', 'fluesopp'],
        },
        ['kantarell', 'fluesopp', 'steinsopp'],
    ) == {'giftige': 1, 'matsopper': 2}
    assert svar.kategoriser_sopper({'giftige': ['fluesopp']}, ['kantarell']) == {}


def test_7():
    assert svar.stigespill([5, 4, 2, 2], {5: 12, 18: 7}) == 9
    assert svar.stigespill([3, 3], {3: 20}) == 23


def test_8():
    assert (
        svar.finn_sopp(
            ['rød', 'stor'],
            ['prikker'],
            {
                'rød': {'prikker': 'fluesopp', 'brune lameller': 'rødskivesopp'},
                'brun': {'prikker': 'sjampinjong'},
            },
        )
        == 'fluesopp'
    )
    assert (
        svar.finn_sopp(
            ['rød', 'brun'],
            ['prikker'],
            {'rød': {'prikker': 'fluesopp'}, 'brun': {'prikker': 'sjampinjong'}},
        )
        == 'uklar'
    )


def test_9():
    assert (
        svar.identifiser_sopp(['rød', 'prikker'], {'rød': {'prikker': 'fluesopp'}})
        == 'fluesopp'
    )
    assert (
        svar.identifiser_sopp(
            ['rød'], {'rød': {'prikker': 'fluesopp', 'brune lameller': 'rødskivesopp'}}
        )
        == 'uklar'
    )


koder = ['K7M2', 'R4X9', 'B8T1', 'N5Q3', 'W2H6', 'D9L4', 'P3V7', 'Z6C1', 'M1F8']

navn = [
    'samme_sopp',
    'tell_giftige',
    'finn_trygg_sopp',
    'jages',
    'flertall',
    'kategoriser_sopper',
    'stigespill',
    'finn_sopp',
    'identifiser_sopp',
]

tester = [test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9]

lost = 0

for i in range(len(tester)):
    try:
        tester[i]()
        print(f'{i + 1}. {navn[i]:<20} GODKJENT     kode: {koder[i]}')
        lost += 1
    except AttributeError:
        print(f'{i + 1}. {navn[i]:<20} IKKE SKREVET ENNÅ')
        break
    except AssertionError:
        print(f'{i + 1}. {navn[i]:<20} FEIL - les oppgaveteksten en gang til')
        break
    except Exception as feil:
        print(f'{i + 1}. {navn[i]:<20} KRASJET - {type(feil).__name__}: {feil}')
        break

print()
print(f'Laget har klart {lost} av 9.')

if lost == 9:
    print('Alle ni! Si fra til læreren.')
