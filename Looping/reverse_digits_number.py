# Reverse the digits of a number 


# input section 
num = int(input('enter the postive number '))
tmp = num
# logic section 
# reverse_digits = num[::-1]
reverse_digits = 0
while num:
    digit = num % 10
    reverse_digits = reverse_digits * 10 + digit
    num //= 10

# display section 
print(f'Number {tmp}, Reverse digits {reverse_digits}')