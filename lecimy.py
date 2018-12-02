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
for i in r_handle:  # loop that is reading every line in a file
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
    elif w(i, "Tytu") or w(i, "Wpłatomat") or w(i, "Operacja") or w(i, "Odbiorca") or w(i, "Nadawca") or w(i, "2018") or w(i, "Prowadzonego") or w(i, "Prowadzony") or w(i, ", POL"):
        w_handle.write(i)
print(str(neg) + "\n" + str(pos))
r_handle.close()
w_handle.close()