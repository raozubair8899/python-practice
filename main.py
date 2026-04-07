import random
import math
            #Taking inputs
lower = int(input("Enter Lower bound: " ))

            #Taking inputs
upper = int(input("Enter the upper bound: " ))

# Generating the random number between the upper bound and lower bound 

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou have only ", total_chances, " chances to guess the integer!\n")

#initializing the number of guesses
count = 0
flag = False

#for calculation of minimum number of guesses depends upon range
while count < total_chances:
    count += 1

#taking guessing number as input
    guess = int(input("Guess a number: " ))

#condition testing
    if x == guess:
        print("Congratulations you did it in " , count, " try")

#once guessed, loop will break
        flag = True
        break
    elif x>guess:
        print("You guessed too small! ")
    elif x<guess:
        print("You guessed too high! ")

#if guessing is more than required guesses, show this output
if not flag:
    print("\nThe number is %d " %x)
    print ("\nBetter luck Next Time! ")
