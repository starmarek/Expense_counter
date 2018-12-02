r_handle = open("Wyciag.txt", "r")  # reading file handle
w_handle = open("Summary.txt", 'w')  # writing file handle


# searches for expression in given line
def w(it, expr):
    b = not (it.find(expr) == -1)
    # if expr is coma, it change it in purpose of comparing similar lines [very needed step]
    if expr == ",":
        it = it.strip("\n")
        it = it.replace(",", "")
        it = it.replace("-", "")
        return it.replace(" ", "").isdigit()
    else:
        return b


neg = 0
pos = 0
mainy = []
nmainy = []
for count, i in enumerate(r_handle, 1):  # loop that is reading every line in a file
    # in the next line, condition that decides about usefulness of text line
    if w(i, ","):
        i = i.split(" ")
        i = float(i.pop(0).replace(",", "."))
        if i < 0:
            neg += i
        else:
            pos += i
        w_handle.write(str(i))
        w_handle.write("\n\n")
        nmainy.append(str(i))
        mainy.append(nmainy.copy())
        nmainy.clear()
    elif w(i, "Tytu") or w(i, "Wpłatomat") or w(i, "Operacja") or w(i, "Odbiorca") or w(i, "Nadawca") or w(i,
                                                                                                           "2018") or w(
            i, "Prowadzonego") or w(i, "Prowadzony") or w(i, ", POL"):
        if count == 1:
            nmainy.append(str(i))
            mainy.append(nmainy.copy())
            nmainy.clear()
            continue
        w_handle.write(i)
        nmainy.append(str(i))

przelewy = []
karta = []
przychody = []
wydatki = []
wplatomat = []
zw_dlugi = []
dlugi = []
mieszkanie = []
pseudowydatki = []
pseudoprzychody = []
spozywcze = []
x = ["biedro", "pss", "zabka", "politechnika", "t and j", "lidl", "mihiderka", "ledi", "karni", "carrefour", "fasolka", ]

for ind in mainy:
    if any("xxxx" in s for s in ind):  # KARTA
        for z in x:
            if any(z in s.lower() for s in ind):
                spozywcze.append(ind)
        if any("RACHWALIK" in s for s in ind) or any("ZUZANNA" in s for s in ind) or any("Lorek" in s for s in ind):
            zw_dlugi.append(ind)
        karta.append(ind)
    else:   # PRZELEWY
        przelewy.append(ind)
        if any("przychodzący" in s for s in ind) or any("Wpłatomat" in s for s in ind):  # PRZYCHODZACE
            przychody.append(ind)
            if any("Wpłatomat" in s for s in ind):
                wplatomat.append(ind)
            elif any("RACHWALIK" in s for s in ind) or any("ZUZANNA" in s for s in ind) or any("Lorek" in s for s in ind):
                zw_dlugi.append(ind)
        else:    # WYCHODZACE
            if any("RACHWALIK" in s for s in ind) or any("ZUZANNA" in s for s in ind) or any("Lorek" in s for s in ind):
                dlugi.append(ind)
            elif any("mzuri" in s for s in ind):
                mieszkanie.append(ind)
            elif any("Wyciąg" in s for s in ind):
                continue
            wydatki.append(ind)
print(spozywcze)

print(str(neg) + "\n" + str(pos))

r_handle.close()
w_handle.close()
