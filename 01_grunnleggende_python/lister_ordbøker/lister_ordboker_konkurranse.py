# IT2 fagdag - runde 1: Hva skriver den ut?
#
# Vis én snutt av gangen på skjerm. Parene skriver svaret på ark.
# Ingen får kjøre koden. Ett poeng per riktig svar.
#
# Fasit står nederst i fila. Ikke bla ned mens du viser.


# Snutt 1

for i in range(3):
    print(i * 2)


# Snutt 2

tall = 17
print(tall / 2)
print(tall // 2)
print(tall % 2)


# Snutt 3

ord_tekst = 'datamaskin'
print(ord_tekst[0])
print(ord_tekst[4:8])
print(ord_tekst[-1])


# Snutt 4

poeng = 60

if poeng > 40:
    print('bestått')
elif poeng > 55:
    print('godt bestått')
else:
    print('ikke bestått')


# Snutt 5

n = 1
sum_tall = 0

while n < 5:
    sum_tall += n
    n += 1

print(sum_tall)


# ============================================================
# FASIT
#
# 1   0, 2, 4
#     range(3) stopper FØR 3.
#
# 2   8.5, 8, 1
#     / gir alltid desimaltall, // runder nedover, % gir resten.
#
# 3   d, mask, n
#     Utsnittet [4:8] tar med 4, 5, 6 og 7 - men ikke 8.
#
# 4   bestått
#     Den andre grenen nås aldri, fordi alt som er større enn 55
#     også er større enn 40. Rekkefølgen er logikken.
#
# 5   10
#     Løkka kjører for n = 1, 2, 3 og 4. Ikke 5.
# ============================================================
