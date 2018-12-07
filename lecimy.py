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

wyrazy_wymiana = []
wyrazy_mat = []
wyrazy_komunikacja = []
wyrazy_skarbonka = []
wyrazy_zw_dlugi = []
wyrazy_dlugi = []
wyrazy_mieszkanie = [
    "mzuri"
]
wyrazy_spozywcze = [
    "biedro",
    "pss",
    "zabka",
    "politechnika",
    "t and j",
    "lidl",
    "mihiderka",
    "ledi",
    "karni",
    "carrefour",
    "fasolka"
]

zbior_wyrazow = [
    wyrazy_spozywcze,
    wyrazy_mieszkanie,
    wyrazy_wymiana,
    wyrazy_mat,
    wyrazy_komunikacja,
    wyrazy_skarbonka,
    wyrazy_zw_dlugi,
    wyrazy_dlugi
]
tmp = []
liczba_wydatkow = 2
i = 0
suma = 0
count = 0


def take_second(elem):
    return elem[1]


def check(str):
    if 'xxxx' in str[0]:
        return 0
    else:
        elo = str[3].strip("\n")
        elo = elo.replace(".", "")
        elo = elo.replace("-", "")
        if elo.replace(" ", "").isdigit():
            return 1
        else:
            return 2


while i < liczba_wydatkow:

    for ind in mainy:
        for s in ind:
            if any(z in s.lower() for z in zbior_wyrazow[i]):
                pomoc = check(ind)
                tmp.append(ind)
                suma += float(ind[2+pomoc])

    tmp.sort(key=take_second)

    for s in tmp:
        pomoc = check(s)
        count += 1
        if count < 10:
            if float(s[2+pomoc]) > -10:
                if s[2][::-1].find('.') == 2:
                    w_handle.write("{}     {}    {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 1 -2.32
                    continue
                w_handle.write("{}     {}    {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 1 -2.3
                continue
            if s[2][::-1].find('.') == 2:
                w_handle.write("{}     {}   {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 1 -12.32
                continue
            w_handle.write("{}     {}    {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 1 -12.3
            continue

        if float(s[2+pomoc]) > -10:
            if s[2][::-1].find('.') == 2:
                w_handle.write("{}    {}    {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 11 -2.32
                continue
            w_handle.write("{}    {}     {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 11 -2.3
            continue
        if s[2][::-1].find('.') == 2:
            w_handle.write("{}    {}   {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 11 -12.32
            continue
        w_handle.write("{}    {}    {}    {}".format(count, s[2 + pomoc], s[0][0:10], s[1]))  # 11 -12.3
        continue

    for d in range(0, 100): w_handle.write('-')
    w_handle.write('\n')
    i += 1
    count = 0
    tmp.clear()


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