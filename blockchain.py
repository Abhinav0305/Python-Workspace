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
    # print(blockchain[0])
     for block in blockchain:
         print('Outputting values')
         print(block)


def verify_chain():
    #block_index=0
    is_valid=True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid=True
        else:
            is_valid=False
    # for block in blockchain:
    #     if block_index ==0:
    #         block_index +=1
    #         continue
    #     elif block[0] == blockchain[block_index -1 ]:
    #         is_valid=True
    #     else:
    #         is_valid=False
    #         break
    #     block_index +=1
    return is_valid




waiting_for_input=True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('3: Quit')
    user_choice=get_user_choice()
    if user_choice == '1':
        tx_amount=get_transactional_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice =='2':
        print_blockchain_elements()
    elif user_choice =='h':
        if len(blockchain)>=1:
            blockchain[0]=[2];
    elif user_choice == '3':
        waiting_for_input=False
    else:
        print('Input was invalid, please pick a value from the list')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break


print('Done!')
