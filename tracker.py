# Expense Tracker Installment 4: tracker makes descisions
# Author: Bryan Kenneth Blando

print('=' * 40) 
print('EXPENSE TRACKER'.center(40))
print('Know where your money goes.'.center(40))
print('=' * 40)

print('\nMAIN MENU')
print(' [1] Add an expense \t\t(coming soon)')
print(' [2] View all expenses \t\t(coming soon)')
print(' [3] Show total spent \t\t(coming soon)')
print(' [4] Exit \t\t\t(coming soon)\n')

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# -----------  input section
# first expense section
item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
first_expense_msg = ''

# Condition
if amount1 > 200: first_expense_msg = 'Huge expense - are you sure? ' 
elif amount1 > 100: first_expense_msg = 'Big expense.'
elif amount1 > 50: first_expense_msg = 'Moderate expense.'
else: first_expense_msg = 'Small expense.'
print(first_expense_msg)

# Second expense section
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
second_expense_msg = ''

# Condition
if amount2 > 200: second_expense_msg = 'Huge expense - are you sure? ' 
elif amount1 > 100 and amount2 > 100: second_expense_msg = 'Two big expenses in a row - slow down.'
elif amount2 > 100: second_expense_msg = 'Big expense.'
elif amount2 > 50: second_expense_msg = 'Moderate expense.'
else: second_expense_msg = 'Small expense.'
print(second_expense_msg)

tax_rate = int(input("Tax Rate %? ")) / 100
budget = int(input('Your budget? '))

# computation
total = amount1 + amount2
average = total / 2
# tax and grand_total computation
tax = (amount1 * tax_rate) + (amount2 * tax_rate)
grand_total = total + tax
# Condition Message
notification_msg = ''

if budget < grand_total: notification_msg = f'Over budget by  ${grand_total - budget}!'
elif grand_total >= (0.90 * budget): notification_msg = f'Careful: only  ${budget - grand_total} left.'
else: notification_msg = f'Within budget:  ${budget - grand_total} left.'
# --------------------------------------->
print(f'\n{'-' * 40}')
print('SUMMARY')
print(f' - {item1 + ':':<10} \t${amount1}')
print(f' - {item2 + ':':<10} \t${amount2}')

print(f'Subtotal: \t${total}')
print(f'Average: \t${average}')
print(f'Tax ({tax_rate * 100}%): \t${tax}')
print(f'Grand total: \t${grand_total}')
print(notification_msg)

print('-' * 40)
print('Made by: Bryan Kenneth Blando | Installment 4')
print('=' * 40)

