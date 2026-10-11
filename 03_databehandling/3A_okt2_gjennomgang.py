# IT2 3A - graftegning, økt 2
# Tilpasning og flere grafer

import matplotlib.pyplot as plt

# 1. Tekst på figuren

maaneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun']
temperatur = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3]

plt.plot(maaneder, temperatur)
plt.title('Middeltemperatur Oslo')
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.show()

# En graf uten aksetitler er ubrukelig. Det er det første sensor ser etter.


# 2. Rutenett og hjelpelinjer

plt.plot(maaneder, temperatur)
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.grid(True)
plt.axhline(0)  # vannrett linje, her nullpunktet
plt.show()


# 3. Begrense aksene

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.plot(x, y)
plt.xlim(0, 5)
plt.ylim(0, 30)
plt.show()

# Dataene er de samme. Bare utsnittet er endret.


# 4. Flere kurver med forklaring

by1 = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3]
by2 = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0]

plt.plot(maaneder, by1, label='Oslo')
plt.plot(maaneder, by2, label='Bergen')
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.legend()
plt.show()

# label= på hver kurve, og legend() til slutt.


# 5. Farge og stil

plt.plot(maaneder, by1, color='tomato', linestyle='--', marker='o', label='Oslo')
plt.plot(maaneder, by2, color='steelblue', marker='s', label='Bergen')
plt.legend()
plt.show()


# 6. Flere figurer ved siden av hverandre

plt.subplot(1, 2, 1)  # 1 rad, 2 kolonner, nummer 1
plt.plot(maaneder, by1)
plt.title('Oslo')

plt.subplot(1, 2, 2)  # nummer 2
plt.plot(maaneder, by2)
plt.title('Bergen')

plt.show()

# subplot(rader, kolonner, nummer) kalles FØR hver graf.


# 7. Lagre figuren som bilde

plt.bar(maaneder, temperatur)
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.savefig('temperatur.png')
plt.show()

# savefig() må stå FØR show(). Etter show() er figuren tom.
