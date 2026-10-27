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
subtotal = 0.0

# first expense section
item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

# Condition
if amount1 > 200: print('Huge expense - are you sure? ')
elif amount1 > 100: print('Big expense.')
elif amount1 > 50: print('Moderate expense.')
else: print('Small expense.')


# Second expense section
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Condition
if amount2 > 200: print('Huge expense - are you sure?') 
elif amount1 > 100 and amount2 > 100: print('Two big expenses in a row - slow down.')
elif amount2 > 100: print('Big expense.')
elif amount2 > 50: print('Moderate expense.')
else: print('Small expense.')

tax_rate = int(input("Tax Rate %? ")) / 100
budget = int(input('Your budget? '))

# computation
average = subtotal / 2
# tax and total computation
tax = (amount1 * tax_rate) + (amount2 * tax_rate)
total = subtotal + tax
# Condition Message
over_budget = ''

if budget < total : over_budget = f'Over budget by  ${total - budget}!'
elif total >= (0.90 * budget): over_budget = f'Careful: only  ${budget - total} left.'
else: over_budget = f'Within budget:  ${budget - total} left.'

# --------------------------------------->
print(f'\n{'-' * 40}')
print('SUMMARY')
print(f' - {item1 + ':':<10} \t${amount1}')
print(f' - {item2 + ':':<10} \t${amount2}')

print(f'Subtotal: \t${subtotal}')
print(f'Average: \t${average}')
print(f'Tax ({tax_rate * 100}%): \t${tax}')
print(f'Grand total: \t${total}')
print(over_budget)

print('-' * 40)
print('Made by: Bryan Kenneth Blando | Installment 4')
print('=' * 40)

