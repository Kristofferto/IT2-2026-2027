# IT2 3A - graftegning, økt 1
# Diagramtypene

import matplotlib.pyplot as plt

# 1. Linjegraf

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()

# plot() tegner. show() viser fram.
# Uten show() skjer det ingenting.


# 2. Punktdiagram

hoyder = [1.62, 1.75, 1.80, 1.69, 1.91, 1.58]
vekter = [58, 72, 85, 64, 94, 52]

plt.scatter(hoyder, vekter)
plt.show()

# scatter() når sammenhengen mellom to målinger er poenget.


# 3. Søylediagram

utdanning = ['ST', 'IM', 'HO', 'EL', 'BA']
antall = [142, 88, 61, 54, 37]

plt.bar(utdanning, antall)
plt.show()

plt.barh(utdanning, antall)  # liggende, bra til lange navn
plt.show()


# 4. Sektordiagram

partier = ['A', 'H', 'SV', 'FrP', 'Sp']
representanter = [48, 36, 13, 21, 28]

plt.pie(representanter, labels=partier)
plt.show()


# 5. Histogram

karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]

plt.hist(karakterer, bins=[1, 2, 3, 4, 5, 6, 7])
plt.show()

# bins bestemmer hvor grensene går.
# Histogram teller hvor mange som havner i hvert intervall.
# Søylediagram viser verdier du allerede har.


# 6. Flere grafer i samme figur

x = [0, 1, 2, 3, 4, 5]
kvadrat = [0, 1, 4, 9, 16, 25]
dobbelt = [0, 2, 4, 6, 8, 10]

plt.plot(x, kvadrat)
plt.plot(x, dobbelt)
plt.show()

# Alt som tegnes før show() havner i samme figur.
