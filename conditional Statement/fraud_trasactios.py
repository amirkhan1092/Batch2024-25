# Problem: Develop a fraud detection system for a bank. The system should flag a transaction as "suspicious" if:
# • The transaction amount exceeds 70% of the account's total balance.
# • The transaction happens after 10 PM (22:00) or before 6 AM (06:00).
# Input: account_balance, transaction_amount, transaction_time (24-hour format)


# input Format
account_balance = eval(input('Enter the account Balance '))

transaction_amount = eval(input('Enter the transaction amount '))

transaction_time = input('Enter the transaction_time in HH:MM:SS Format ')

hh, mm, ss = transaction_time.split(':')
hh = int(hh)
mm = int(mm)
ss = int(ss)


if transaction_amount>=(account_balance*0.7) or hh>=22 or hh=<6:
    print("non safe")
else:
    print('safe') 
