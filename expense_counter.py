"""Expense Counter

This file allows the users of Getin Noble Bank to print out their expenses
in the appropriete (sorted) order, based on the end-of-month bank statement.

Before usage it NEEDS to be adjusted to the user, by adding it's very own words for expenses into the lists.

The bank statemnt itself must be raw copied (Ctrl+A + Ctrl+C + Ctrl+V) to the 'statement.txt' file.
This file must be saved in the same folder as the following python (.py) file.
Program saves the produced data in the created 'outcome.txt' file.
"""

from builtins import enumerate
from typing import Union

# 8 lists of words. Each one represnts a specific kind of expense.
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

# stores all the lists with their own access keys
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
    A class used to represent a bank expense
    That means every kind of money transaction that you make in the bank

    Attributes:
        amount (float): represents how much money you have spend or got in the given expense
        reciever (str): person or institution that recieves money throughout the given expense
        date (str): date when the expense was made

    Variables:
        kind (int): keyword from dictionary that represents kind of the expense in refernece to
                     types of expenses that are desribed in the introduction to the program
        num_of_str_in_amount (int): stores number of chars in the amount attribute.
                                     Later it will be used for setting proper text layout in outcome.txt file.

    Methods:
        set_kind (): sets 'kind' variable for given object
        prin_yrsl (): prints out the objects insides in a specific way
    """

    kind = str

    num_of_str_in_amount = int

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        self.amount = amount
        self.reciever = reciever
        self.date = date
        self.num_of_str_in_amount = len(str(amount))

    def set_kind(self) -> None:
        """Sets 'kind' variable which is a representation of type of an expense.
            Method loops through the dictionary and if 'self.reciever' contains the word from any
            dictionary's variable it saves its key as a 'self.kind'.

        Returns:
            None: method is used only to set the 'kind' variable.

        Raises:
            Exception: if the 'kind' varaible was not set (it happens mainly if self.reciever contains
                        word which is not in words lists, so the update is needed).
        """
        for KEY, VALUE in words.items():
            if any(z in self.reciever.lower() for z in VALUE):
                # following if's made to distinguish debts from debts_return
                if KEY == 'debts' and self.amount > 0:
                    continue
                if KEY == 'debts_return' and self.amount < 0:
                    continue
                self.kind = KEY
                return
        raise Exception('Kind of an object was not set')

    def prin_yrsl(self, handle, max_len_amount: int, max_len_reciever: int, *args) -> None:
        """Writes out the most important information about the object.

        Parameters:
            handle (io.TextIO): file handle
            max_len_amount (int): length in chars of the longest 'amount' attribute throughout all expenses
            max_len_reciever (int): the same as previous, but this time 'reciever' attribute

        Returns:
            None: method is used only to write out information
        """

        spaces = (max_len_amount - self.num_of_str_in_amount + 2) * ' '
        # 'if' made for cooperation with overriden method in the child class
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
        length_of_reciever (int): length in chars of the 'reciever' attribute. Only this class needs this variable
                                    because it is used for proper 'title' attribute layout in the 'outcome.txt' file.
        +other inherited variables

    Methods:
        prin_yrsl (): expanded functionality of parents method
        +other inherited methods
    """

    length_of_reciever = int

    def __init__(self, amount: float, reciever: str, title: str, date: str) -> None:
        super().__init__(amount, reciever, date)
        self.title = title
        self.length_of_reciever = len(reciever)

    def prin_yrsl(self, handle, max_num_amount, max_len_reciever, *args):
        """It forces the parent method in the super() call to use special behavior. That is because it passes
            the extra 'spy' variable witch triggers 'if' statement. This happens in order to deleating an
            unwanted newline symbol. Additionally it writes out information about the title
            because only tansfers do have this attribute.
        """
        spy = int
        super().prin_yrsl(handle, max_num_amount, max_len_reciever, spy)
        handle.write(f'{(max_len_reciever - self.length_of_reciever + 2) * " "}{self.title}')


class CardPayment(Expense):
    """
    A derived class used to represent a Card Payment
    It inherits from Expense class

    Attributes:
        only inherited attributes

    Variables:
        only inherited variables

    Methods:
        only inherited methods
    """

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        super().__init__(amount, reciever, date)


class CashMachine(Expense):
    """
    A derived class used to represent a Cash Machine transaction that means money payment or payout.
    It inherits from Expense class

    Attributes:
        only inherited attributes

    Variables:
        only inherited variables

    Methods:
        only inherited methods
    """

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        super().__init__(amount, reciever, date)


def decide_if_is_amount(foo: str) -> bool:
    """Processes the input and decides wheater it is an amount of an expense

    Parameters:
        foo (str): one line from the bank statement

    Returns:
        bool: true if the line is an amount; false if it isn't
    """

    # following procedure will leave only digits in lines with amount of an expense
    foo = foo.strip("\n")
    foo = foo.replace(",", "")
    foo = foo.replace("-", "")
    return foo.replace(" ", "").isdigit()


def create_object(expense: list) -> Union[CashMachine, CardPayment, Transfer]:
    """Processes the raw expense from list and creates the
        appropriete object then returns it.

    Parameters:
        expense (list): one raw expense

    Returns:
        Union[CashMachine, CardPayment, Tranasfer]: object of an appropriete expense

    Raises:
        Exception: Information that some expenses werent coverted to objects which is a result of
         not finding a keyword in the raw expense
    """

    reciever = int
    title = int
    # card payment
    if any('xxxx' in foo.lower() for foo in expense):
        return CardPayment(float(expense[-1]), expense[1], expense[0][:11])
    # transfer
    elif any('przelew' in foo.lower() for foo in expense):
        for indexx, part in enumerate(expense):
            # finding lines with following information and saving index
            if 'tytu' in part.lower():
                title = indexx
            if ('prowadzon' in part.lower()) or ('odbiorca' in part.lower()) or ('nadawca' in part.lower()):
                reciever = indexx
        return Transfer(float(expense[-1]), expense[reciever], expense[title][8:], expense[0][:11])
    # cash machine
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
        list: nested list of expenses (objects)
    """

    add_to_list = False
    foo = list()
    expenses = list()
    for line in handle:
        if ('2018' in line) and not ('za okres' in line):
            add_to_list = True
        # if true, loop is in expense appending mode
        if add_to_list:
            # if found amount line, then its final line of an expense and appending mode is going off
            if decide_if_is_amount(line):
                line = line.split(" ").pop(0).replace(',', '.')
                foo.append(line)
                instance = create_object(foo)
                instance.set_kind()
                expenses.append(instance)
                foo.clear()
                add_to_list = False
                continue
            foo.append(line)
    return expenses


def writeout_expenses(list_of_onekind_objects: list, list_of_onekind_words: list, handle, max_amou: int,
                      max_reciever: int) -> None:
    """Function writes to the file given list of objects. At the end of each type (list must be already sorted by type)
        it also writes the amount of money spent on those expenses (objects). The preasumption is, that list of words
        and list of objects passed to the function are containing content which relates to the expenses
        of the same kind (for example both relates to the food expenses).

        Function detects the end of each type by checking if the expense-matching word is already in dictionary.

    Parameters:
        list_of_onekind_objects (list): list of expenses (objects) that are sorted by type and relates to the same kind
                                        of expense as the passed list of words.
        list_of_onekind_words (list): list of words (look at the lists at the begining of file) that relates to the same
                                        kind of expense as passed list of expenses.
        handle (io.TextIO): file handle
        max_amou (int): max length of amount among all expenses. Counted by chars.
        max_reciever (int): the same as above but concerning reciever attribute.

    Returns:
        None: function is used only for writing out to the file.

    Raises:
        Exception: warning that inputed lists are not mathcing. That is because, after inner loop exhausted
         it didnt find the any word in given object.
    """

    foo = dict()
    counter = 0
    for position, objectt in enumerate(list_of_onekind_objects):
        for word in list_of_onekind_words:
            if word in objectt.reciever.lower():
                # then this is end of last type and its time to sum it up
                if not(word in foo):
                    foo[word] = 1
                    # in first loop the word is obviously not in dictionary so that is a fail alarm
                    if position == 0:
                        break
                    handle.write('SUM: ' + str(counter) + 2 * '\n')
                    counter = 0
                # cleaning the dictionary to avoid recurrence of words and missunderstanding
                if foo.__len__() == 2:
                    foo.pop(list(foo.keys())[0])
                break
        else:
            raise Exception('Lists are not matching so the particular SUMS are not beeing written out')
        counter += objectt.amount
        objectt.prin_yrsl(handle, max_amou, max_reciever)
    # there is no further loops so it's needed to sum up last type
    handle.write('SUM: ' + str(counter) + '\n')


def make_outcome(handle, lista):
    summator = 0
    positives = 0
    negatives = 0
    max_amou = sorted(lista, key=lambda x: x.num_of_str_in_amount).pop().num_of_str_in_amount
    max_reciever = sorted(lista, key=lambda x:
                          x.length_of_reciever if type(x) == Transfer else False).pop().length_of_reciever

    for key, value in words.items():
        handle.write(60 * ' ' + str(key).upper() + 2 * '\n')
        tmp = sorted([expense for expense in lista if expense.kind == key], key=lambda x: x.reciever.lower())
        for num in tmp:
            summator += num.amount
        if summator > 0:
            positives += summator
        else:
            negatives += summator
        writeout_expenses(tmp, value, handle, max_amou, max_reciever)
        handle.write(55 * ' ' + f'SUM FOR {str(key).upper()}: ' + str(summator) + '\n')
        summator = 0
        handle.write(125 * '-' + 2 * '\n')
    handle.write(60 * ' ' + 'SUMMARY\n' + f'Negatives: {round(negatives, 2)}' + 37 * ' ' +
                 f'Positives: {round(positives, 2)}' + 30 * ' ' + f'Balance: {round(negatives + positives, 2)}')


def main():
    with open('Statement.txt', 'r') as read_handle:
        expenses_list = sorted(process_list(read_handle), key=lambda x: x.kind)

    with open("Outcome.txt", 'w') as write_handle:
        make_outcome(write_handle, expenses_list)


if __name__ == '__main__':
    main()
# TODO: counting the in n out expenses
