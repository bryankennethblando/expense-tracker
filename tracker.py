# Expense Tracker Installment 1: Landing Page
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

# input section
item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
tax_rate = int(input("Tax Rate %? ")) / 100
budget = int(input('Your budget? '))

# --------------------------------------->
print(f'\n{'-' * 40}')
print('SUMMARY')
print(f' - {item1}: \t${amount1}')
print(f' - {item2}: \t${amount2}')

# computation
total = amount1 + amount2
average = total / 2

# tax and grand_total computation
tax = (amount1 * tax_rate) + (amount2 * tax_rate)
grand_total = total + tax
over_budget = grand_total > budget
left_in_budget = budget - grand_total

print(f'Total spent: \t${total}')
print(f'Average: \t${average}')
print(f'Tax ({tax_rate}%): \t${tax}')
print(f'Grand total: \t${grand_total}')
print(f'Over budget? \t{over_budget}')
print(f'Left in budget: ${left_in_budget}')

print('-' * 40)
print('Made by: Bryan Kenneth Blando | Installment 3')
print('=' * 40)

