'''1. Check Voting Eligibility
Problem: Write a program to check if a person is eligible to vote. A person can vote if they
are 18 years or older and have a valid voter ID.
Example:
Input: age = 20, has_voter_id = Yes
Output: "Eligible to vote"
Input: age = 16, has_voter_id = No
Output: "Not eligible to vote"'''

# input section 
age = int(input("enter your age ")) 
voter_id = input(" you have voter id Yes/No ")

# logic Section 
out = age >= 18  and voter_id == 'Yes'
x=out*"you are eligile for voting"+(1-out)*"you are not eligible for voting"
print(x)
# Display Section 