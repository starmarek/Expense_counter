r_handle = open("Wyciag.txt", "r")
w_handle = open("Summary.txt", 'w')


def w(it, expr):
    if expr == ",":
        it = it.strip("\n")
        it = it.replace(",", "")
        it = it.replace("-", "")
        return it.replace(" ", "").isdigit()
    return not(it.find(expr) == -1)


mainy = []
nmainy = []
slowa_klucz = [
    "Tytu",
    "Wpłatomat",
    "Operacja",
    "Odbiorca",
    "Nadawca",
    "2018",
    "Prowadzonego",
    "Prowadzony",
    ", POL"
]

for i in r_handle:

    if w(i, ","):
        i = i.split(" ")
        i = float(i.pop(0).replace(",", "."))
        nmainy.append(str(i))
        mainy.append(nmainy.copy())
        nmainy.clear()

    elif any(s in i for s in slowa_klucz) and not("Wyciąg" in i):
        nmainy.append(str(i))

wyrazy_wymiana = [
    "pucher",
    "wpłatomat",
    "pekao",
    "okw nr"
]
wyrazy_mat = [
    "ikea",
    "carto",
    "apteka",
    "phu beata",
    "blik",
    "poczta",
    "media",
    "castorama",
    "salon fry"
]
wyrazy_komunikacja = [
    "interc",
    "ancard",
    "skycash"
]
wyrazy_skarbonka = [
    "zachowaj re"
]
wyrazy_zw_dlugi = [
    "lorek",
    "zuzanna",
    "rachwalik",
    "jarosz",
    "dyba",
    "księżyk",
    "alicja"

]
wyrazy_dlugi = wyrazy_zw_dlugi
wyrazy_mieszkanie = [
    "mzuri"
]
wyrazy_spozywcze = [
    "biedr",
    "pss",
    "zabka",
    "politechnika",
    "and j",
    "lidl",
    "mihiderka",
    "ledi",
    "karni",
    "carrefour",
    "fasolka",
    "szu rlej",
    "przybij",
    "zeni t",
    "hats off",
    "mel & di",
    "padbar"
]

zbior_wyrazow = [
    wyrazy_spozywcze,
    wyrazy_mieszkanie,
    wyrazy_skarbonka,
    wyrazy_komunikacja,
    wyrazy_wymiana,
    wyrazy_mat,
    wyrazy_zw_dlugi,
    wyrazy_dlugi
]
tmp = []
liczba_wydatkow = 8
i = 0
suma = 0
count = 0
counter = 0
counterer = 0

def take_second(elem):
    return elem[1]


def checknsave(str):
    for l, g in enumerate(str):
        if "." in g:
            g = g.strip("\n")
            g = g.replace(".", "")
            g = g.replace("-", "")
            if g.replace(" ", "").isdigit():
                return l


# TODO: string backwards indexing
# TODO: sort dates
# TODO: titles of transfers

while i < liczba_wydatkow:

    for ind in mainy:
        for s in ind:

            if any(z in s.lower() for z in zbior_wyrazow[i]):
                if i == 6 and 'wychodzący' in ind[0].lower():
                    continue
                elif i == 7 and 'przychodzący' in ind[0].lower():
                    continue
                tmp.append(ind)

    tmp.sort(key=take_second)
    counterer += len(tmp)
    for s in tmp:
        pomoc = checknsave(s)

        count += 1
        ll = len(str(s[pomoc]))
        b = s[1]
        if pomoc == 1:
            b = s[0][22:31] + "\n"

        if count < 10:
            if ll == 3:
                w_handle.write("{}   {}        {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 4:
                w_handle.write("{}   {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 5:
                w_handle.write("{}   {}      {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 6:
                w_handle.write("{}   {}     {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 7:
                w_handle.write("{}   {}    {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32

        elif ll == 3:
            w_handle.write("{}   {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
        elif ll == 4:
            w_handle.write("{}  {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
        elif ll == 5:
            w_handle.write("{}  {}      {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
        elif ll == 6:
            w_handle.write("{}  {}     {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
        elif ll == 7:
            w_handle.write("{}  {}    {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
    w_handle.write("-"*100+"\n")
    i += 1
    counter += count
    count = 0
    tmp.clear()

w_handle.write(str(counterer))
w_handle.write(str(counter))



r_handle.close()
w_handle.close()


# /////////////////////////////CZESC INTERAKTYWNA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# expenses = [
#     "Artykuly spozywcze", "Czynsz za mieszkanie", "Zwroty dlugow",
#     "Moje dlugi"
# ]
#
#
# switcher = {
#     1: spozywcze,
#     2: mieszkanie,
#     3: zw_dlugi,
#     4: dlugi
# }
#
#
# def oblicz():
#     wynik = 0
#     nazwy = []
#     liczby = []
#     daty = []
#     if switcher.get(wybor) == spozywcze:
#         for i in spozywcze:
#             wynik += float(i[2])
#             nazwy.append(i[1])
#             liczby.append(i[2])
#             daty.append(i[0][0:10])
#     elif switcher.get(wybor) == mieszkanie:
#         for i in mieszkanie:
#             wynik += float(i[3])
#     elif switcher.get(wybor) == zw_dlugi:
#         for i in zw_dlugi:
#             wynik += float(i[3])
#     elif switcher.get(wybor) == dlugi:
#         for i in dlugi:
#             wynik += float(i[3])
#     for l,s in enumerate(nazwy, 1):
#         print('{}   {}     {}    {}'.format(l, liczby[l-1], daty[l-1], s.replace("\n", "")))
#     print("\nSumaryczna ilosc pieniedzy: " + str(wynik) + "\n")
#
#
# def wyswietl():
#
#     print(switcher.get(wybor , "lipa"))
#
#
# while True:
#     print("--------------------------")
#     for a, b in enumerate(expenses, 1):
#         print('{} {}'.format(a, b))
#     wybor = int(input("\nProsze podac numer informacji do wyswietlenia: "))
#     if wybor == 99:
#         break
#     oblicz()