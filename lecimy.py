"""Expense Counter

This file allows the users of Getin Noble Bank to print out their expenses
in the appropriete (sorted) order, based on the end-of-month bank statement.

The bank statemnt itself must be raw copied (Ctrl+A + Ctrl+C + Ctrl+V) to the 'statement.txt' file.
This file must be saved in the same folder as the following python (.py) file.
Program saves the produced data in the created 'outcome.txt' file.
"""
from builtins import enumerate
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
    "orkana",
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
    'rent': rent,
    'food': food,
    'debts': debts,
    'debts_return': debts_return,
    'transport': transport,
    'real': real,
    'exchange': exchange,
    'piggybank': piggybank
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

    kind = str

    num_of_str_in_amount = int

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        self.amount = amount
        self.reciever = reciever
        self.date = date
        self.num_of_str_in_amount = len(str(amount))

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
                if key == 'debts' and self.amount > 0:
                    continue
                if key == 'debts_return' and self.amount < 0:
                    continue
                self.kind = key
                return
        raise Exception('Kind of an object was not set')

    def prin_yrsl(self, handle, num, elo, *args):
        spaces = (num - self.num_of_str_in_amount + 2) * ' '
        if args:
            handle.write('{} {}{}{} '.format(self.date, self.amount, spaces, self.reciever.strip('\n')))
            return
        handle.write(f'{self.date} {self.amount}{spaces}{self.reciever}')


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

    length_of_reciever = int

    def __init__(self, amount: float, reciever: str, title: str, date: str) -> None:
        super().__init__(amount, reciever, date)
        self.title = title
        self.length_of_reciever = len(reciever)

    def prin_yrsl(self, handle, num, elo, *args):
        spy = int
        spacesss = (elo - self.length_of_reciever + 2) * ' '
        super().prin_yrsl(handle, num, elo, spy)
        write_handle.write(f'{spacesss}{self.title}')


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

    reciever = int
    title = int
    if any('xxxx' in foo.lower() for foo in expense):
        return CardPayment(float(expense[-1]), expense[1], expense[0][:11])
    elif any('przelew' in foo.lower() for foo in expense):
        for indexx, e in enumerate(expense):
            if 'tytu' in e.lower():
                title = indexx
            if ('prowadzon' in e.lower()) or ('odbiorca' in e.lower()) or ('nadawca' in e.lower()):
                reciever = indexx
        return Transfer(float(expense[-1]), expense[reciever], expense[title][8:], expense[0][:11])
    elif any('ata got' in foo.lower() for foo in expense) or any('ata kart' in foo.lower() for foo in expense):
        return CashMachine(float(expense[-1]), expense[-2], expense[0][:11])
    else:
        print('This is an expense that caused all the trouble --> ' + str(expense))
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
        if ('2018' in line) and not ('za okres' in line):
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


def spaceee(objekt, wordsy, handle):
    second = {}
    summator = 0
    for c, t in enumerate(objekt):
        for g in wordsy:
            if g in t.reciever.lower():
                if not(g in second):
                    second[g] = 1
                    if c == 0:
                        continue
                    handle.write('SUM: ' + str(summator) + 2 * '\n')
                    summator = 0
                if second.__len__() == 2:
                    second.pop(list(second.keys())[0])
        summator += t.amount
        t.prin_yrsl(write_handle, max_amou, max_reciever)
    handle.write('SUM: ' + str(summator) + '\n')


with open('Statement.txt', 'r') as read_handle:
    expenses_list = sorted(process_list(read_handle), key=lambda x: x.kind)

max_amou = sorted(expenses_list, key=lambda x: x.num_of_str_in_amount).pop().num_of_str_in_amount
max_reciever = sorted(expenses_list, key=lambda x: x.length_of_reciever if type(x) == Transfer else False).pop().length_of_reciever


with open("Outcome.txt", 'w') as write_handle:
    summator = 0
    for key, value in words.items():
        write_handle.write(60 * ' ' + str(key).upper() + 2 * '\n')
        tmp = sorted([expense for expense in expenses_list if expense.kind == key], key=lambda x: x.reciever.lower())
        for num in tmp:
            summator += num.amount
        spaceee(tmp, value, write_handle)
        write_handle.write(55 * ' ' + f'SUM FOR {str(key).upper()}: ' + str(summator) + '\n')
        summator = 0
        write_handle.write(125*'-'+ '\n')

        #TODO: summary of negatives and positives + comments + cleaning