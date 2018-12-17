"""Expense Counter

This file allows the users of Getin Noble Bank to print out their expenses
in the appropriete (sorted) order, based on the end-of-month bank statement.

The bank statemnt itself must be raw copied (Ctrl+A + Ctrl+C + Ctrl+V) to the 'statement.txt' file.
This file must be saved in the same folder as the following python (.py) file.
Program saves the produced data in the created 'outcome.txt' file.
"""


from typing import Union


exchange = [
    "pucher",
    "pekao",
    "miasto katowice",
    "pasaz"
]
real = [
    "ikea",
    "carto",
    "apteka",
    "phu beata",
    "pay",
    "poczta",
    "media",
    "castorama",
    "salon fry"
]
transport = [
    "city",
    "ancard",
    "skycash"
]
piggybank = [
    "getin noble"
]
debts_return = [
    "lorek",
    "zuzanna",
    "rachwalik",
    "jarosz",
    "dyba",
    "księżyk",
    "alicja"

]
debts = debts_return
rent = [
    "mzuri"
]
food = [
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

words = {
    1: rent,
    2: food,
    3: debts,
    4: debts_return,
    5: transport,
    6: real,
    7: exchange,
    8: piggybank
}


class Expense:
    """
    A class used to represent an bank expense
    That means every kind of money transaction that you make in the bank

    Attributes:
        amount (float): represents how much money you have spend or got in the given expense
        reciever (str): person or institution that recieves money throughout the given expense
        date (str): date when the expense was made

    Variables:
        kind (int): keyword from dictionary that represents kind of the expense in refernece to
                     types of expenses that are desribed in the introduction to the program

    Methods:
        set_kind (dict_Words (dict)): sets 'kind' variable for given object
    """

    kind = int

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        self.amount = amount
        self.reciever = reciever
        self.date = date

    def set_kind(self, dict_words: dict) -> None:
        """It sets 'kind' variable which is a representation of type of an expense.
            Method loops through the dictionary and if 'self.reciever' contains the word from given
            dictionary variable it saves its key as a 'self.kind'.

        Parameters:
            dict_words (dict): dictionary which contains keys to lists of words. Each words list
                                contains only words which are referenced to the specific expense type.
        Returns:
            None: method is used only to set the 'kind' variable

        Raises:
            Exception: if the 'kind' varaible was not set (it happens mainly if self.reciever contains
                        word which is not in words lists, so the update is needed).
        """
        for key, value in dict_words.items():
            if any(z in self.reciever.lower() for z in value):
                if key == 3 and self.amount > 0:
                    continue
                if key == 4 and self.amount < 0:
                    continue
                self.kind = key
                return
        raise Exception('Kind of an object was not set')


class Transfer(Expense):
    """
    A derived class used to represent a bank transfer
    It inherits from Expense class

    Attributes:
        title (str): the title of a transfer
        +other that are inherited

    Variables:
        only inherited variables
    """

    def __init__(self, amount: float, reciever: str, title: str, date: str) -> None:
        super().__init__(amount, reciever, date)
        self.title = title


class CardPayment(Expense):
    """
    A derived class used to represent a Card Payment
    It inherits from Expense class

    Attributes:
        only inherited attributes

    Variables:
        only inherited variables
    """

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        super().__init__(amount, reciever, date)


class CashMachine(Expense):
    """
    A derived class used to represent a Cash Machine transaction,
    that means money payment or payout
    It inherits from Expense class

    Attributes:
        only inherited attributes

    Variables:
        only inherited variables
    """

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        super().__init__(amount, reciever, date)


def decide_if_is_amount(foo: str) -> bool:
    """Processes the input by the special algorithm and
        and decides wheater it is an amount of an expense

    Parameters:
        foo (str): one line from the bank statement

    Returns:
        bool: true if the line is an expense; false if it isn't
    """

    foo = foo.strip("\n")
    foo = foo.replace(",", "")
    foo = foo.replace("-", "")
    return foo.replace(" ", "").isdigit()


def create(expense: list) -> Union[CashMachine, CardPayment, Transfer]:
    """Processes the raw expense from list and creates the
        appropriete object then returns it.

    Parameters:
        expense (list): one raw expense

    Returns:
        Union[CashMachine, CardPayment, Tranasfer]: object of an appropriete expense

    Raises:
        Exception: Information that some exceptions werent coverted to objects which is a result of
         not finding a keyword in the raw expense
    """

    reciever = str
    title = str
    if any('xxxx' in foo.lower() for foo in expense):
        return CardPayment(float(expense[-1]), expense[1], expense[0][:11])
    elif any('przelew' in foo.lower() for foo in expense):
        for indexx, e in enumerate(expense):
            if 'tytułem' in e.lower():
                title = indexx
            if ('prowadzon' in e.lower()) or ('odbiorca' in e.lower()) or ('nadawca' in e.lower()):
                reciever = indexx
        return Transfer(float(expense[-1]), expense[reciever], expense[title], expense[0][:11])
    elif any('wpłata' in foo.lower() for foo in expense) or any('wypłata' in foo.lower() for foo in expense):
        return CashMachine(float(expense[-1]), expense[-2], expense[0][:11])
    else:
        raise Exception('Some expenses werent converted to objects')


def process_list(handle) -> list:
    """Loops through the bank statement and creates
         nested list of expenses

    Parameters:
        handle (io.TextIO): file handle

    Returns:
        list: nested list of expenses - objects if beeing exact
    """

    add_to_list = False
    foo = list()
    expenses = list()
    for line in handle:
        if ('2018' in line) and not ('Wyciąg' in line):
            add_to_list = True
        if add_to_list:
            if decide_if_is_amount(line):
                line = line.split(" ")
                line = line.pop(0).replace(',', '.')
                foo.append(line)
                instance = create(foo)
                instance.set_kind(words)
                expenses.append(instance)
                foo.clear()
                add_to_list = False
                continue
            foo.append(line)
    return expenses


with open('Statement.txt', 'r') as read_handle:
    expenses_list = process_list(read_handle)


######################
tmp = []
liczba_wydatkow = 8
i = 0
suma = 0
count = 0
counter = 0
counterer = 0
second = ''


def take_second(elem):
    return elem[1].lower()


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

with open("Outcome.txt", 'w') as write_handle:
    while i < liczba_wydatkow:
        for ind in expenses_list:
            for s in ind:

                if any(z in s.lower() for z in zbior_wyrazow[i]):
                    if i == 6 and 'wychodzący' in ind[0].lower():
                        continue
                    elif i == 7 and 'przychodzący' in ind[0].lower():
                        continue
                    tmp.append(ind)

        tmp.sort(key=take_second)  # TODO: change sorting, so it uses the keywords
        counterer += len(tmp)
        for s in tmp:
            pomoc = checknsave(s)
            for t in s:
                for g in zbior_wyrazow[i]:
                    if g in t.lower():
                        first = g
                        if first == second:
                            continue
                        elif second == '':
                            second = first
                            continue
                        elif count == 0:
                            second = first
                            continue
                        else:
                            write_handle.write('\n')
                        second = first

            count += 1
            ll = len(str(s[pomoc]))
            b = s[1]
            if pomoc == 1:
                b = s[0][22:31] + "\n"

            if count < 10:
                if ll == 3:
                    write_handle.write("{}   {}        {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
                elif ll == 4:
                    write_handle.write("{}   {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
                elif ll == 5:
                    write_handle.write("{}   {}      {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
                elif ll == 6:
                    write_handle.write("{}   {}     {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
                elif ll == 7:
                    write_handle.write("{}   {}    {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32

            elif ll == 3:
                write_handle.write("{}   {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 4:
                write_handle.write("{}  {}       {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 5:
                write_handle.write("{}  {}      {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 6:
                write_handle.write("{}  {}     {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
            elif ll == 7:
                write_handle.write("{}  {}    {}    {}".format(count, s[pomoc], s[0][0:10], b))  # 11 -2.32
        write_handle.write("-" * 100 + "\n")
        i += 1
        counter += count
        count = 0
        tmp.clear()

    write_handle.write(str(counterer))
    write_handle.write(str(counter))


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