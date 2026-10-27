# Expense Tracker Installment 5: menu comes alive
# Author: Bryan Kenneth Blando

print('=' * 40) 
print('EXPENSE TRACKER'.center(40))
print('Know where your money goes.'.center(40))
print('=' * 40)

name = input("What's your name? ")
tax_percent = int(input("Tax Rate %? ")) / 100
budget = int(input('Your budget? '))
print(f'Welcome, {name}!')

choice = 0
count = 0
subtotal = 0.0
while choice != 4:
    print('\nMAIN MENU')
    print(' [1] Add an expense')
    print(' [2] View all expenses \t\t(coming soon)')
    print(' [3] Show total spent')
    print(' [4] Exit\n')

    choice = int(input('Choose 1-4: '))

    if choice == 1:
        # -----------  input section
        amount = float(input("Amount? "))
        subtotal += amount

        # Condition
        if amount > 200: print('  Huge expense - are you sure?')
        elif amount > 100: print('  Big expense.')
        elif amount > 50: print('  Moderate expense.')
        else: print('  Small expense.')

        count += 1

    elif choice == 2: 
        print('  Coming Soon: tracker can\'t remember each item yet')

    elif choice == 3: 
        # tax and total computation
        tax_percent *= subtotal
        total = subtotal + tax_percent
        # Condition Message
        over_budget = ''

        if budget < subtotal : over_budget = f'  Over budget by ${total - budget}!'
        elif subtotal >= (0.90 * budget): over_budget = f'  Careful: only ${budget - total} left.'
        else: over_budget = f'  Within budget: ${budget - total} left.'

        # --------------------------------------->
        print(f'  Expenses: \t {count}')
        print(f'  Subtotal: \t ${subtotal}')
        print(f'  Tax ({tax_percent}%): \t ${tax_percent}')
        print(f'  Grand total: \t ${total}')
        print(over_budget)

    elif choice > 4 or choice < 1:
        print('  Please choose 1, 2, 3, or 4.')

    else:
        print(f'Goodbye, {name}!')
        print('-' * 40)
        print('Made by: Bryan Kenneth Blando | Installment 5')
        print('=' * 40)

