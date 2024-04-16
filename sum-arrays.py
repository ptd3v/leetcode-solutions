# Sum Arrays - CodeWars (8th Kyu)
# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Example Data
numbers = [1,2,3,6,78,8] # Single data type only

# Solution 1 (Sum Function)
def sum_array(numbers):
    if not numbers: # Error handling for empty array
        return 0
    return sum(numbers)

print(sum_array(numbers)) # Outputs the sum total of the array, solution 1.

# Solution 2 (For Loop)
def sum_loop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_loop(numbers)) # Outputs the sum total of the array, solution 2.

# Outputs
print(numbers) # Outputs the array contents
print(sum_array) # Outputs the memory location of the array