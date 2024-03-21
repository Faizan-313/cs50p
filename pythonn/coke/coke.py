print('Amount Due: 50')
coins = [25,10,5]

amount_due = 50
coins_added = 0
while True:
    insert_coin = int(input('Insert Coin: '))
    if insert_coin in coins:
        amount_due -= insert_coin
        coins_added += insert_coin
    else:
       print(f'Amount Due: {amount_due}')

    if coins_added >= 50:
        print(f'Change Owed: {coins_added - 50}')
        break
    else:
        print(f'Amount Due: {amount_due}')