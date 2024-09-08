# ATM
# input section 
amount = int(input('Enter the amount '))-100

# logic
twok = amount // 2000
amount = amount % 2000
fiveh = amount // 500
amount = amount % 500
twoh = amount // 200
amount = amount % 200
oneh =  amount // 100


# display 
print('Two Thausand Notes', twok)
print('Five Hundred Notes', fiveh)
print('Two Hundred Notes', twoh)
print('One Hundred Notes', oneh+1)
