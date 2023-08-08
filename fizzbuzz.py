#Interview Essentials 1: FizzBuzz
#Overview: Print a range of numbers. If a number is divisible by x, print A. If a number if divisible by y, print B. If a number if divisible by x and y, print AB.
#Purpose: To asses a candidate's basic programming skills and problem-solving abilities.
#Skills Required: Problem Solving, Logic, Modulo, Loops, Conditional Statements.

#Create a loop for numbers between 0 and 20.
for number in range (0,20):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  else
    print(number)
