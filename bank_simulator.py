# The four primary menu calls of View 
# Balance, 
# Credit, 
# Debit, 
# and Exit 
# are linked to function calls
'''
This function serves as a main menu
'''
from fastnumbers import isfloat
def main_menu():
    choice = 'Y'
    while choice == 'Y':
        user_choice = input('=======================\n'
                            'enter 1 to view Balance\n'
                            'enter 2 to add money\n'
                            'enter 3 to withdraw money\n'
                            'enter 4 to Exit\n'
                            '=======================\n')
        if user_choice =='1':
            choice = Balance(choice)
            
        elif user_choice == '2':
            choice = Credit(choice)
        elif user_choice == '3':
            choice = Debit(choice)
        elif user_choice == '4':
            break
        else:
            print('Please choose a number 1 through 4')


def Balance(choice):
    with open('money_file.txt', 'r') as money:
        current_amount = money.readline()
        print('You currently have $' + str(current_amount))
    return Exit(choice)


'''
this funciton allows the user to add money into the account
'''
def Credit(choice):
    with open('money_file.txt', 'r') as money:
        current_amount = money.readline()
    while True:
        money_added = input('How much money do you wish to add?')

        if isfloat(money_added) and float(money_added) == round(float(money_added), 2):
            new_total = float(current_amount) + float(money_added)

            with open('money_file.txt', 'w') as money_deposit:
                money_deposit.write(str(round(new_total,2)))
            break
        else:
            print('Please input a proper selection!')

    with open('money_file.txt', 'r') as money:
        current_amount = money.readline()
        print('You currently have $' + str(current_amount))
    return Exit(choice)


'''
This function allows the user to take away money from the account
'''
def Debit(choice):
    with open('money_file.txt', 'r') as money:
        current_amount = money.readline()

    while True:
        
        money_added = input('How much money do you wish to withdraw?')
        
        if isfloat(money_added) and float(money_added) == round(float(money_added), 2):
            new_total = float(current_amount) - float(money_added)

            with open('money_file.txt', 'w') as money_deposit:
                money_deposit.write(str(round(new_total,2)))
            break
        else:
            print('Please input a proper selection!')

    with open('money_file.txt', 'r') as money:
        current_amount = money.readline()
        print('You currently have $' + str(current_amount))
    return Exit(choice)


'''
This function allows the user to exit or continue the program
'''
def Exit(choice):

    while True:
        user_continue = input('Do you wish to continue?\n')

        if user_continue.lower() in ['y', 'yes']:
            choice = 'Y'
            return choice
        elif user_continue.lower() in ['n', 'no']:
            choice = 'n'
            return choice
        else:
            print('You did no input a proper selection\n'
                'type y or yes to continue\n'
                'type n or no to Exit')


main_menu()