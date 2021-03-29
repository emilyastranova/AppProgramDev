#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        try:
            test_score = float(test_score)
        except ValueError:
            print("Invalid data type, try again...")
    else:
        break
    try:
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print("Test score must be from 0 through 100. Score discarded. Try again.")   
    except TypeError:
        pass # No need to print anything out, this exists to handle what remains of the loop

# calculate average score
try:
    average_score = round(score_total / counter)
except ZeroDivisionError:
    print("No valid data was inputted... Exiting now")
    exit()
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")


