<<<<<<< HEAD
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
=======
# IT2 1B - Valg og betingelser
# Oppgaver: se boka
# Marker en seksjon og kjør med Shift+Enter.


# 1. En betingelse er sann eller usann

alder = 17

print(alder > 18)  # False
print(alder < 18)  # True
print(alder == 17)  # == er sammenligning, = er tilordning
print(alder != 17)  # ulik
print(alder >= 17)
print(type(alder > 18))  # bool


# 2. if

alder = 20

if alder >= 18:
    print('Du kan stemme.')

print('Dette skrives ut uansett.')

# Kolon på slutten av if-linja.
# Innrykket avgjør hva som hører til. Fire mellomrom.


# 3. if - else

temperatur = 3

if temperatur < 0:
    print('Det er minusgrader.')
else:
    print('Det er plussgrader.')


# 4. if - elif - else

poeng = 78  # input('Poeng: ')

if poeng >= 90:
    karakter = 6
elif poeng >= 75:
    karakter = 5
elif poeng >= 60:
    karakter = 4
elif poeng >= 40:
    karakter = 3
else:
    karakter = 2

print(f'{poeng} poeng gir karakteren {karakter}.')

# Python sjekker ovenfra og ned og stopper ved første som er sann.
# Derfor må grensene komme i riktig rekkefølge.


# 5. and, or, not

alder = 20
har_billett = True

if alder >= 18 and har_billett:
    print('Velkommen inn.')

if alder < 18 or not har_billett:
    print('Beklager.')

# and  -> begge må være sanne
# or   -> minst én må være sann
# not  -> snur True til False

print(True and False)
print(True or False)
print(not True)


# 6. Nøstet if

vaer = 'sol'
temperatur = 22

if temperatur > 20:
    if vaer == 'sol':
        print('Bading.')
    else:
        print('Tur.')
else:
    print('Innendørs.')

# Samme sak med and, ofte lettere å lese:
if temperatur > 20 and vaer == 'sol':
    print('Bading.')


# 7. Feller

# = er tilordning, == er sammenligning
# if alder = 18:     -> SyntaxError

# input() gir tekst, ikke tall
svar = '20'
print(svar == 20)  # False - tekst er ikke tall
print(int(svar) == 20)  # True

# Tekst sammenlignes bokstav for bokstav, og store bokstaver teller
print('Kari' == 'kari')
print('Kari'.lower() == 'kari')

# in sjekker om noe finnes inni
print('sol' in 'solskinn')

# Python tillater doble sammenligninger
alder = 15
print(0 < alder < 18)

# Desimaltall skal ikke sammenlignes med ==
print(0.1 + 0.2 == 0.3)  # False!
>>>>>>> ebf9c6c3b899643e10abf57c8e90320b85347cb2
