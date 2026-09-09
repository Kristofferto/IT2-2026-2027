# Betingelser
alder = 20
print(alder < 30)
print(alder > 30)
print(alder == 20)
print(alder != 20)
print(alder >= 17)

# if setninger
alder = 20
if alder < 10:
    print('Du er yngre enn 10 år!')
elif alder == 10:
    print('Du er akkurat 10 år!')
elif alder > 10:
    print('Du er eldre enn 10 år.')
else:
    # dette er alle andre tilfeller
    # print('ettellerannet)
    print('oiwghw')

# lag nå en kode for å sjekke om en person med gitt alder skal ha barne, ungdom, voksen eller honnør billett hos ruter

alder = int(input('Hvor gammel er du? '))

if alder < 6:
    print('Gratis.')
elif alder < 18:
    print('Ungdom.')
elif alder < 67:
    print('Voksen.')
else:
    print('Honnør.')


spm = input('Har du billett? ').lower()
if spm == 'ja':
    harBillett = True
else:
    harBillett = False

if alder >= 18 or harBillett:
    print('Velkommen!')
else:
    print('Nej..')

sant = True
print(not sant)
