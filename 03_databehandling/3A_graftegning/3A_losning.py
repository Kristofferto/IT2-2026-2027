'''
IT2 3A - LØSNINGSFORSLAG

Alle figurer kommenteres bort nederst i hver oppgave hvis du vil
kjøre hele fila uten å klikke deg gjennom alle vinduene.
'''

import matplotlib.pyplot as plt

'''
3A OPPGAVE 2 - fra løkke til graf
'''

x = []
kvadrat = []
kube = []

for i in range(21):
    x.append(i)
    kvadrat.append(i**2)
    kube.append(i**3)

plt.plot(x, kvadrat, label='x^2')
plt.plot(x, kube, label='x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('To potensfunksjoner')
plt.legend()
plt.ylim(0, 400)
plt.show()

# e) x^3 forsvinner ut av bildet etter x = 7. Dataene er der,
#    men utsnittet skjuler dem.


'''
3A OPPGAVE 3 - karakterer
'''

karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]

plt.hist(karakterer, bins=[1, 2, 3, 4, 5, 6, 7])
plt.xlabel('karakter')
plt.ylabel('antall')
plt.title('Fordeling')
plt.show()

fordeling = {}
for k in karakterer:
    if k in fordeling:
        fordeling[k] += 1
    else:
        fordeling[k] = 1

verdier = sorted(fordeling)
antall = []
for k in verdier:
    antall.append(fordeling[k])

plt.bar(verdier, antall)
plt.xlabel('karakter')
plt.ylabel('antall')
plt.show()

# d) Histogram teller selv. Søylediagram tegner tall du allerede har.
#    Har du rådata, bruk histogram. Har du en oppsummering, bruk bar.


'''
3A OPPGAVE 5 - to byer
'''

maaneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun',
            'jul', 'aug', 'sep', 'okt', 'nov', 'des']
oslo = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3, 18.0, 16.8, 12.4, 6.9, 1.5, -1.8]
bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0, 14.1, 14.2, 11.5, 8.4, 4.3, 2.1]

plt.plot(maaneder, oslo, linestyle='--', marker='o', label='Oslo')
plt.plot(maaneder, bergen, marker='s', label='Bergen')
plt.axhline(0)
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.title('Middeltemperatur')
plt.legend()
plt.show()

# d) største forskjell
storst = 0
maaned_storst = ''
forskjell = []

for i in range(len(maaneder)):
    diff = oslo[i] - bergen[i]
    forskjell.append(diff)
    if abs(diff) > storst:
        storst = abs(diff)
        maaned_storst = maaneder[i]

print(f'Størst forskjell i {maaned_storst}: {storst:.1f} grader')

plt.bar(maaneder, forskjell)
plt.axhline(0)
plt.xlabel('måned')
plt.ylabel('Oslo minus Bergen')
plt.show()


'''
3A OPPGAVE 6 - subplot
'''

plt.subplot(1, 2, 1)
plt.plot(maaneder, oslo)
plt.title('Oslo')
plt.ylim(-5, 20)

plt.subplot(1, 2, 2)
plt.plot(maaneder, bergen)
plt.title('Bergen')
plt.ylim(-5, 20)

plt.show()

# c) Lik y-akse er det som gjør figurene sammenlignbare.
#    Uten den ser Bergen ut til å svinge like mye som Oslo.
