# Armstrong 

num = int(input('Enter the positive Integer Value '))
tmp = num
# '''
# len = 3
# 2 ^ len + 3 ^ len + 4 ^ len == 234
# '''
len = 0 
while num:
    num //= 10
    len += 1
num = tmp
# print(f'{len=}')
s = 0
while num:
    d = num % 10
    s += d ** len
    num //= 10

# print(f'{s=}')

if s == tmp:
    print(tmp, 'is Armstrong Number')
else:
    print('Not an Armstrong Number')