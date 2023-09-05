#Interview Essentials 1: FizzBuzz
#Overview: Print a range of numbers. If a number is divisible by x, print A. If a number if divisible by y, print B. If a number if divisible by x and y, print AB.
#Purpose: To asses a candidate's basic programming skills and problem-solving abilities.
#Skills Required: Problem Solving, Logic, Modulo, Loops, Conditional Statements.

#Create a loop for numbers between 0 and 20.
for num in range(1, 21):
    #Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")  #If divisible by both 3 and 5, print "FizzBuzz"
    #Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")  #If divisible by 3, print "Fizz"
    #Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")  #If divisible by 5, print "Buzz"
    else:
        print(num) #If not divisible by either 3 or 5, print the number itself

#Challenge One (Contributions Welcome)
for num in range (1,000):
    #For every FizzBuzz below 10 (numbers divisible by 3 and 5), we get 3, 5, 6 and 9.
    #Added together, we get 23. Your task is to add every FizzBuzz under 1,000 together.

#You are welcome to use any language you want, please create your own seperate file in the repo.
