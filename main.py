# The following codes may help you to do your assignment on Python programing:

# Send a welcome message to the new team member in DSC 510 program

print("Welcome everyone to the DSC 510!")

# Retrieve first name of the team members
first_name = input("May I know your first name please?: ")

# Retrieve from the team members the number of books they purchased in this semester.

number_of_books = int(input("Enter the number of books you bought in this semester: "))


# Calculate the total cost of buying books for each member
cost_per_book = 20
total_cost = number_of_books * cost_per_book

# Print a receipt for the user
print("\nReceipt for", first_name)
print("Number of books bought by the team member:", number_of_books)
print("Total cost of buying book: $", total_cost)

#Change#:1
#Change(s) Made: Added date and time handling to show current date and time on the receipt input lines 31-37 added
#Date of Change: 9/7/2023
#Author: zd ghj
#Change Approved by: sddff ghhhh
#Date Moved to Production: 9/7/2023

import datetime
# Get the current date and time
current_date_time = datetime.datetime.now()
# Format the date and time as a string
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
# Print the formatted date and time
print("Current date and time:", formatted_date_time)
