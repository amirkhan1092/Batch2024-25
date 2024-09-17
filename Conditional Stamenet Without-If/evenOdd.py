# Even Odd without if else 

# inout section
a = int(input("Enter the number :"))

# logic section 
out = a%2 == 0

x = out*"number is even " + (1-out)* "number is odd"
print (x)