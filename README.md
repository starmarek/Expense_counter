# Expense_counter
The project is all about counting up and printing out in the appropriete order and manner all the expenses included in the inputed bank statement.

## How does it work at the moment
- Inputed bank statement must be a __raw copied .txt file__ (Example in the _Statement.txt_).
- Program uses the 'lists of words' which are included in the code to distinguish expenses from each other. Before usage these lists must be __adjusted to the user__. If not, program won't work properly, or won't work at all.
- Program creates new .txt file and saves output right there.

## Versions of program
					
					 			1.0

- Program gets a .txt file with raw text copied from bank statement
- It returns also a .txt file with ordered, sorted and divided into groups expenses. Expenses will be listed in the following categories and order:
1. Food	
2. Rent
3. Piggybank money
4. My debts
5. Return of debts
6. Transport
7. Money exchange between me and my parents and also myself
8. Money spended on real things and services (hairdresser, school accessories, electronics, etc.)

- These will be separeted with long '------' line and signed with the name of it; expenses that are releted to the same person or institution will be next to each other and changing the institution will result in adding an endline mark.

- At the end of given institution expenses, after each category and after reading every expense in the bank
statement, there will be an amount of money displayed, summarizing given piece of data.

								2.0

- Adding GUI and possibilty for user to add his own kind of expenses.
- Changing the system of 'lists of words' to something more reliable and comfy to use.

## Authors

- Aleksander Pucher -> initial idea and first lines of code 
