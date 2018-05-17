blockchain = []


def get_last_blockchain_value():
    """ Returns the last value"""
    if len(blockchain) < 1:
        return None
    else:
        return blockchain[-1]


def add_value(transaction_amount,last_transaction=[1]):
    if last_transaction == None:
        last_transaction=[1]
    blockchain.append([last_transaction,transaction_amount]);


def get_transactional_value():
    user_input=float(input('Your transaction amount please '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting values')
        print(block)







while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit')
    user_choice=get_user_choice()
    if user_choice == '1':
        tx_amount=get_transactional_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice =='2':
        print_blockchain_elements()
    elif user_choice == '3':
        break
    else:
        print('Input was invalid, please pick a value from the list')

