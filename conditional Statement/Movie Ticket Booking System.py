# Movie Ticket Booking System
# input section
age = int(input("Enter age "))
display_ticket_price = int(input("Enter Ticket price: "))
is_3d_movie = input("Is Movie 3d Yes/No ")


 #logic section
if age < 12:
   display_ticket_price /= 2
elif age >=60:
  display_ticket_price -= display_ticket_price*0.3

if is_3d_movie == 'Yes':
   display_ticket_price += 5

# Output Section 
print('Ticket Price', display_ticket_price, '$')