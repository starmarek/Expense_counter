"""Expense Counter

This file allows the users of Getin Noble Bank to print out their expenses
in the appropriete (sorted) order, based on the end-of-month bank statement.

Before usage make sure to adjust 'list_of_words.py' to the user!

The bank statemnt itself must be raw copied (Ctrl+A + Ctrl+C + Ctrl+V) to the 'Statement.txt' file.
This file must be saved in the same folder as the following python (.py) file.
Program saves the produced data in the created 'Outcome.txt' file.
"""

from builtins import enumerate
from typing import Union
from lists_of_words import words


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
                                     It will be used for setting proper text layout in outcome.txt file.
        original_count_of_expenses (int): controls the amount of expenses that originally were included in the
                                          statement.
        processed_count_of_expenses (int): controls the amount of expenses that are actually printed for the user.
        max_len_amount (int): stores the number of chars for the longest 'amount' attribute among all objects.

    Methods:
        set_kind (): sets 'kind' variable for given object
        prin_yrsl (): prints out the objects insides in a specific way
    """
    original_count_of_expenses = 0

    processed_count_of_expenses = 0

    kind = str

    num_of_str_in_amount = int

    max_len_amount = 0

    def __init__(self, amount: float, reciever: str, date: str) -> None:
        """Besides standard initialization, function also updates the 'max_len_amount' variable if its needed"""

        self.amount = amount
        self.reciever = reciever
        self.date = date
        self.num_of_str_in_amount = len(str(amount))
        if Expense.max_len_amount < self.num_of_str_in_amount:
            Expense.max_len_amount = self.num_of_str_in_amount

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
        else:
            raise Exception('Kind of this object was not set   ->   ' + self.date + self.reciever)

    def prin_yrsl(self, handle) -> None:
        """Writes out the most important information about the object.

        Parameters:
            handle (io.TextIO): file handle

        Returns:
            None: method is used only to write out information
        """
        Expense.processed_count_of_expenses += 1
        spaces = (Expense.max_len_amount - self.num_of_str_in_amount + 2) * ' '
        handle.write('{} {}{}{}'.format(self.date, self.amount, spaces, self.reciever.strip('\n')))


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
         max_len_amount (int): stores the number of chars for the longest 'reciever' attribute among all objects.
        +other inherited variables

    Methods:
        prin_yrsl (): expanded functionality of parents method
        +other inherited methods
    """

    length_of_reciever = int

    max_len_reciever = 0

    def __init__(self, amount: float, reciever: str, title: str, date: str) -> None:
        """Besides standard initialization, function also updates the 'max_len_reciever' variable if its needed"""

        super().__init__(amount, reciever, date)
        self.title = title
        self.length_of_reciever = len(reciever)
        if Transfer.max_len_reciever < self.length_of_reciever:
            Transfer.max_len_reciever = self.length_of_reciever

    def prin_yrsl(self, handle):
        """Additionally it writes out information about the title because only tansfers do have this attribute"""

        super().prin_yrsl(handle)
        spaces = (Transfer.max_len_reciever - self.length_of_reciever + 2) * " "
        handle.write('{} {}'.format(spaces, self.title.strip('\n')))


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
    A derived class used to represent a Cash Machine transaction that means money payin or payout.
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
    """Processes the input and decides whether it is an amount of an expense (number representing spended or recieved
        money).

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
        Exception: Information that expense wasnt coverted to object which is a result of
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
            # Looping through and finding appropriate indexes. This operation is needed because in transfers, reciever
            # and title lines are not as regular as in other types of expenses.
            if 'tytu' in part.lower():
                title = indexx
            if ('prowadzon' in part.lower()) or ('odbiorca' in part.lower()) or ('nadawca' in part.lower()):
                reciever = indexx
        return Transfer(float(expense[-1]), expense[reciever], expense[title][9:], expense[0][:11])
    # cash machine
    elif any('ata got' in foo.lower() for foo in expense) or any('ata kart' in foo.lower() for foo in expense):
        return CashMachine(float(expense[-1]), expense[-2], expense[0][:11])
    else:
        raise Exception('This expense wasnt converted into object -> ' + str(expense))


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
    actual_year = handle.readline()[-11:-7]
    for line in handle:
        if actual_year in line:
            add_to_list = True
        # if true, loop is in expense appending mode
        if add_to_list:
            # if found amount line, then its final line of an expense and appending mode is going off
            if decide_if_is_amount(line):
                Expense.original_count_of_expenses += 1  # Keeping track of every expense that should be created
                line = line.split(" ").pop(0).replace(',', '.')  # changing the line with amount into more reliable form
                foo.append(line)
                instance = create_object(foo)
                instance.set_kind()
                expenses.append(instance)
                foo.clear()
                add_to_list = False
                continue
            foo.append(line)
    return expenses


def writeout_expenses(list_of_onekind_objects: list, list_of_onekind_words: list, handle) -> None:
    """Function writes to the file, given piece of the whole list of objects. At the end of each
        institution (list must be sorted by institution already) it also writes the amount of money spent on those
        expenses (objects). The preasumption is, that list of words and list of objects passed to the function are
        containing content which relates to the expenses of the same kind (for example both relates to the
        food expenses).

        Function detects the end of each institution by checking if the expense-matching word is already in dictionary.

    Parameters:
        list_of_onekind_objects (list): list of expenses (objects) that are sorted by institution and relates to the
                                        same kind of expense as the passed list of words.
        list_of_onekind_words (list): list of words (look at imported module) that relates to the same
                                      kind of expense as passed list of expenses.
        handle (io.TextIO): file handle


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
                # then this is end of last institution and its time to sum it up
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
                # breaking out of loop because institution of given object is detected (word is matching)
                break
        else:
            raise Exception('Lists are not matching so the particular SUMS are not beeing written out')
        counter += objectt.amount
        objectt.prin_yrsl(handle)
        handle.write('\n')
    # there is no further loops so it's needed to sum up last institution
    handle.write('SUM: ' + str(counter) + '\n')


def make_outcome(handle, lista: list) -> None:
    """Function is a connector for others. It conducts the process of writing out
        to a file, which is printng out the expenses list and summarizing the expenses after each kind and at the end.

    Parameters:
        handle (io.TextIO): file handle
        lista (list): list of expneses

    Returns:
        None: function is used only for printing out to a file.

    """
    summator = 0  # to sum up all the expenses in the actually list
    positives = 0  # to sum up all incomes
    negatives = 0  # to sum up all outcomes

    for key, value in words.items():
        # name of a kind
        handle.write(60 * ' ' + str(key).upper() + 2 * '\n')
        # creating a list which contains only one kind which is sorted by instances
        tmp = sorted([expense for expense in lista if expense.kind == key], key=lambda x: x.reciever.lower())
        # counting up the exnpenses before writing out
        for num in tmp:
            summator += num.amount
        if summator > 0:
            positives += summator
        else:
            negatives += summator
        writeout_expenses(tmp, value, handle)
        # sum for given kind
        handle.write(55 * ' ' + f'SUM FOR {str(key).upper()}: ' + str(summator) + '\n')
        summator = 0
        handle.write(125 * '-' + 2 * '\n')
    # summarizon at the end of a statement
    handle.write(60 * ' ' + 'SUMMARY\n' + f'Negatives: {round(negatives, 2)}' + 37 * ' ' +
                 f'Positives: {round(positives, 2)}' + 30 * ' ' + f'Balance: {round(negatives + positives, 2)}' +
                 2 * '\n' + 12 * ' ' +
                 f'Expenses included in the original statement: {Expense.original_count_of_expenses}' +
                 + 10 * ' ' + f'Expenses processed by program: {Expense.processed_count_of_expenses}')


def main():
    # creating unsorted list of expenses (objects) from the statement file
    with open('Statement.txt', 'r') as read_handle:
        expenses_list = process_list(read_handle)

    # writing out to the outcome file
    with open("Outcome.txt", 'w') as write_handle:
        make_outcome(write_handle, expenses_list)


if __name__ == '__main__':
    main()
