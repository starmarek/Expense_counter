b = ("760,00 977,28")
b = b.replace(",", "")
b = b.replace("-", "")
print(b.replace(" ", "").isdigit())