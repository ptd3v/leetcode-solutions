# Highest and Lowest (7th Kyu)

# Solution One
def high_and_low(numbers):
    num_list = numbers.split()  # Split the string into a list of numbers
    num_list = [int(num) for num in num_list]  # Convert the string numbers to integers
    max_num = max(num_list)  # Find the highest number
    min_num = min(num_list)  # Find the lowest number
    return f"{max_num} {min_num}"

# Solution Two: Advanced
def high_and_low(numbers):
    list = [int(num) for num in numbers.split()]
    return f"{max(list)} {min(list)}"


# Solution Three: Community
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))