"""
IT2 3A - OPPGAVER
Graftegning

Hver figur skal ha tittel og aksetitler. Uten det er den ikke ferdig.
"""

"""
1. FØRSTE GRAF

    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 4, 9, 16, 25]

  a) Tegn en linjegraf
  b) Legg på tittel og aksetitler
  c) Tegn den samme sammenhengen som punktdiagram i stedet
  d) Tegn begge to i samme figur
"""
"""
2. FRA LØKKE TIL GRAF

  a) Lag to lister med en løkke: x fra 0 til 20, og y som er x i andre
  b) Tegn grafen
  c) Legg til en kurve for x opphøyd i tredje, i samme figur
  d) Sett på forklaring med label og legend
  e) Begrens y-aksen til 0-400. Hva skjer med den bratteste kurven?
"""
"""
3. KLASSENS KARAKTERER

    karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]
  a) Tegn et histogram med bins fra 1 til 7
  b) Tell hvor mange som har hver karakter, med ordbok og løkke
  c) Tegn det samme som søylediagram ut fra tellingen din
  d) Hva er forskjellen på de to figurene? Når passer hver av dem?
"""
"""
4. VALGRESULTAT
    partier = ['A', 'H', 'SV', 'FrP', 'Sp', 'V', 'MDG']
    stemmer = [26.3, 20.4, 7.6, 11.6, 13.5, 4.6, 3.9]
  a) Tegn et sektordiagram med partinavn som labels
  b) Tegn det samme som liggende søylediagram
  c) Hvilken av dem er lettest å lese av nøyaktig? Hvorfor?
  d) Sorter søylene fra størst til minst før du tegner
"""
"""
5. TO BYER
    maaneder = ['jan','feb','mar','apr','mai','jun','jul','aug','sep','okt','nov','des']
    oslo =   [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3, 18.0, 16.8, 12.4, 6.9, 1.5, -1.8]
    bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0, 14.1, 14.2, 11.5, 8.4, 4.3, 2.1]
  a) Tegn begge kurvene i samme figur, med forklaring
  b) Legg på en vannrett linje ved null grader
  c) Gi Oslo stiplet linje og Bergen heltrukket
  d) Finn med løkke hvilken måned forskjellen er størst
  e) Tegn forskjellen mellom byene som en egen kurve
"""


"""
6. SUBPLOT

Bruk dataene fra oppgave 5.

  a) Lag en figur med to grafer ved siden av hverandre, én per by
  b) Gi hver av dem egen tittel
  c) Sett samme y-akse på begge, så de kan sammenlignes
  d) Prøv fire grafer i et 2x2-rutenett
"""


"""
7. LAGRE FIGUREN

  a) Lag en figur du er fornøyd med og lagre den som png
  b) Sjekk at bildet faktisk dukker opp i mappa
  c) Flytt savefig til ETTER show(). Hva skjer, og hvorfor?
"""


"""
8. HAR DU KOMMET GJENNOM ALT?

Terningstatistikk
    Kast to terninger 10 000 ganger, tell hver sum, og tegn
    fordelingen som søylediagram. Ser den ut som du ventet?

Funksjonsplotter
    Lag en funksjon tegn_graf(f, start, slutt) som tegner en hvilken
    som helst matematisk funksjon i et intervall. Test med np.sin.

Din egen
    Finn et datasett du selv bryr deg om og tegn én god figur av det.

Oppgaver Aunivers
    Se også på oppgaver i Aunivers!
"""


# Dere kan også skrive matte i plots!
# Prøv selv når dere løser oppgavene over!

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2


x = np.arange(0, 10)

plt.plot(x, f(x), linestyle='--', label=r'$f(x) = x^2$', marker='s')
plt.legend(loc='lower right')
plt.title(r'$f(x) = x^2 $ for $x \in [0,10]$')
plt.xlabel(r'x')
plt.ylabel(r'$f(x)$')
plt.show()
