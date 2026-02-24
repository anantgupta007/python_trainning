# Create list of 20 numbers
numbers = [1, 5, 3, 7, 5, 9, 5, 2, 8, 5, 4, 6, 5, 10, 11, 5, 12, 13, 5, 14]

print("Original List:", numbers)

# Take input from user
num = int(input("Enter number to delete (except first occurrence): "))

# Check if number exists
if num in numbers:
    first_index = numbers.index(num)   # find first occurrence
    
    # Count occurrences
    count = numbers.count(num)
    
    # Remove remaining occurrences
    for i in range(count - 1):
        numbers.remove(num)
    
    print("Updated List:", numbers)

else:
    print("Number not found in list.")