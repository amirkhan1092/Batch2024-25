# Password Strength 

# Input Section 
pas = input("Enter Password: ")

# logic Section 
out = len(pas) >= 8

# Output Section 

print(out*"Password is strong" + (1-out)\
      *"Password is weak")