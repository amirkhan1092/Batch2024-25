coding questions that focus on **for loops** and **while loops** in Python, designed to challenge students with real-world applications.

---

### 1. **Inventory Management System**
**Problem**: A store manager needs to update the stock quantities for multiple products in the store's inventory. Write a program to iterate over a list of product names and their current quantities, and for each product, add a restock quantity if the product is low on stock (less than 5 units).

**Input**: 
- A list of tuples with product name and current quantity.
- Restock quantity.

**Example**:
```python
Input: inventory = [("Apples", 3), ("Bananas", 12), ("Oranges", 4)], restock_quantity = 10
Output: Updated Inventory: [("Apples", 13), ("Bananas", 12), ("Oranges", 14)]
```

**Hint**: Use a `for` loop to iterate over the list of tuples.

---

### 2. **Automated Email Sender**
**Problem**: Create a program to simulate sending personalized emails to a list of users. For each user in the list, print a message saying "Email sent to [user_name]". If the user has already received an email (indicated by a flag), skip that user.

**Input**:
- A list of tuples with user names and a boolean flag indicating if they have received an email.

**Example**:
```python
Input: users = [("Alice", False), ("Bob", True), ("Charlie", False)]
Output: 
Email sent to Alice
Email sent to Charlie
```

**Hint**: Use a `for` loop and `if` condition to check the flag.

---

### 3. **Bank ATM Withdrawal Limit Checker**
**Problem**: Develop a program that simulates ATM withdrawals. The user is prompted to enter the amount they wish to withdraw. If the amount is above the daily limit of $1000, show an error message. The program should keep allowing the user to make withdrawals until the daily limit is reached.

**Input**:
- Withdrawal amounts entered by the user until the daily limit is reached.

**Example**:
```python
Input: 
Enter amount to withdraw: 300
Enter amount to withdraw: 500
Enter amount to withdraw: 400
Output: 
Withdrawal successful. Remaining limit: $700
Withdrawal successful. Remaining limit: $200
Error: Daily limit exceeded!
```

**Hint**: Use a `while` loop with a counter for the daily limit.

---

### 4. **Password Strength Checker**
**Problem**: Write a program to check the strength of a list of passwords. A password is considered strong if it has at least one uppercase letter, one lowercase letter, one digit, and one special character. Print "Strong Password" for each valid password and "Weak Password" for each invalid password.

**Input**: 
- A list of passwords to be checked.

**Example**:
```python
Input: passwords = ["Hello123!", "weakpass", "Str0ng@123"]
Output: 
Strong Password
Weak Password
Strong Password
```

**Hint**: Use a `for` loop to iterate over the list and nested loops/conditions to check each password.

---

### 5. **Restaurant Order Processing**
**Problem**: In a restaurant, orders are placed in a queue. Write a program to process the orders until no orders are left. For each order, print "Order [order_number] is being processed". The program should stop when all orders are processed.

**Input**:
- A list of order numbers.

**Example**:
```python
Input: orders = [101, 102, 103, 104]
Output: 
Order 101 is being processed
Order 102 is being processed
Order 103 is being processed
Order 104 is being processed
```

**Hint**: Use a `while` loop to iterate until the list is empty.

---

### 6. **Daily Step Counter**
**Problem**: Write a program to track daily step counts. The user enters their step count each day for a week. If the daily step count is less than 5000, print a motivational message to walk more. At the end of the week, print the average step count.

**Input**:
- Step counts for 7 days.

**Example**:
```python
Input: steps = [4000, 6000, 5500, 3000, 4500, 7000, 8000]
Output: 
Day 1: Walk more, you can do it!
Day 4: Walk more, you can do it!
Day 5: Walk more, you can do it!
Average steps this week: 5428.57
```

**Hint**: Use a `for` loop to iterate through the list and calculate the average.

---

### 7. **Prime Number Generator**
**Problem**: Write a program to generate all prime numbers between 1 and a given number `n`. A prime number is a number greater than 1 that has no divisors other than 1 and itself.

**Input**:
- A positive integer `n`.

**Example**:
```python
Input: n = 20
Output: Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19
```

**Hint**: Use a `for` loop to iterate through each number and a nested `for` loop to check for divisors.

---

### 8. **Expense Tracker**
**Problem**: Write a program to track monthly expenses. The user enters their expense each day until they choose to stop. If the total expense exceeds a budget limit, print a warning message. At the end, display the total expense.

**Input**:
- Daily expenses entered by the user until they choose to stop.

**Example**:
```python
Input: 
Enter expense: 100
Enter expense: 200
Enter expense: 150
Stop (entered by user)
Output: 
Total expense: 450
```

**Hint**: Use a `while` loop to keep adding expenses until the user chooses to stop.

---

### 9. **Book Lending System**
**Problem**: Implement a book lending system where a user can borrow books from the library. The library has a list of available books. When a user borrows a book, remove it from the list. If the book is not available, print a message. The process continues until the user chooses to stop.

**Input**:
- A list of available books and the user’s choice to borrow.

**Example**:
```python
Input: books = ["Python Basics", "Data Science 101", "Algorithms"]
Borrow: "Python Basics"
Borrow: "Machine Learning" (not available)
Output: 
"Python Basics" borrowed successfully.
"Machine Learning" is not available.
```

**Hint**: Use a `while` loop with a condition to keep checking for available books.

---

### 10. **Vending Machine Simulator**
**Problem**: Design a vending machine simulator that allows a user to select items and pay for them. The user can enter the item number and quantity. If the user doesn’t have enough balance, print a message. The user can add more money or choose to exit. Display the remaining balance after each purchase.

**Input**:
- Item prices and initial balance.

**Example**:
```python
Input: 
Items: {"Chips": 2, "Soda": 1.5, "Chocolate": 3}
Balance: 5
Choose item: "Chips", Quantity: 1
Choose item: "Soda", Quantity: 2 (Insufficient balance)
Output: 
Purchase successful! Remaining balance: $3.0
Insufficient balance! Please add more money.
```

**Hint**: Use a `while` loop to keep the vending machine running until the user exits.

---

### Key Learning Points:
- These problems involve scenarios requiring loops to manage multiple iterations based on conditions.
- Students will learn to use both `for` and `while` loops effectively, manage conditions, and handle user inputs dynamically.