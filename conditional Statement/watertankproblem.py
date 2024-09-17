h = 10  # height
r = 5  # Radius
F = 15  # Flow rate

t = float(input('Enter the time for the pump to be ON '))

Vtank = 3.14 * r ** 2 * h
Vwtr = F * t

if Vtank > Vwtr:
    print('Tank is Underflow')
elif Vtank == Vwtr:
    print('Tank is Full')
else:
    print('Tank is Overflow')