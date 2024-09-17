# Movie Ticket price after discount 

# input section 
age = int(input('Enter the age: '))
listed_ticket_price = float(input('Enter the ticket price '))
is_3d = input('Is Moview 3D Y/N ')

if age < 12:
    listed_ticket_price /= 2
elif age >= 60:
    listed_ticket_price -= listed_ticket_price * .3

if is_3d == 'Y':
    listed_ticket_price += 5

print('Final Ticket Price', listed_ticket_price)
