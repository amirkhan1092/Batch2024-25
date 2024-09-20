# Number of digits in a number(Integer)

# input section 
num = int(input('Enter the positive Integer Value '))
# num = str(num)
tmp = num
# logic sectin
# out = len(num)
out = 0
while num:
    num = num // 10
    out += 1


# display section 
print(f'Total digits in number {tmp} is {out}')
# 4