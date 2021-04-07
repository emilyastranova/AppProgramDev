#!/usr/bin/env python3
# Test Scores Lab - Tyler Harrison

# Initialize variables
score_total = 0
score1 = 0
score2 = 0
score3 = 0

# Define getScore function
# Returns the input score
def getScore():
    tempScore = int(input("Enter test score: "))
    while tempScore > 100 or tempScore < 0:
        print("Test score must be from 0 through 100. Try again.")
        tempScore = int(input("Enter test score: "))
    return tempScore

# Display Intro prompt
print("\nEnter 3 test scores")
print("======================")

# Get and assign scores from user to variables
score1 = getScore()
score2 = getScore()
score3 = getScore()

# Add up all the scores
score_total = score1 + score2 + score3
# Calculate average score
average_score = round(score_total / 3)
# format and display the result
print("======================")
print("Your Scores:", score1, score2, score3, sep=' ')
print("Total Score:", score_total,"\nAverage Score:", average_score)