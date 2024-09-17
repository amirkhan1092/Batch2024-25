

# input section 
account_balance = float(input('Enter the premium'))
transaction_amount = float(input('Enter the amount for transaction '))
t_time = int(input('Enter the time in integer Hrs only 24 format: 1-24 '))

# logic 

if (account_balance * 0.7)  < transaction_amount:
    pass
elif t_time > 22 or t_time < 6:
    pass
else:
    print('Everything is safe ')
