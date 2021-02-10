#!/usr/bin/env python3
# BMI Calculator Lab - Tyler Harrison

print("The Body Mass Index Calculator")

def getBMI():
    # Get user input
    height = float(input("\nEnter height (in inches): "))
    weight = float(input("Enter weight (in lbs): "))

    # Caluclate BMI
    bodyMassIndex = round(weight / (height * height) * 703, 1)
    weightCategories = { 
        0: "Underweight", 
        1: "Normal", 
        2: "Overweight",
        3: "Obese" 
    }
    if bodyMassIndex < 18.5: # Underweight
        weightStatus = weightCategories.get(0)
    elif bodyMassIndex >=18.5 and bodyMassIndex <=24.9: # Normal
        weightStatus = weightCategories.get(1)
    elif bodyMassIndex >= 25.0 and bodyMassIndex <= 29.9: # Overweight
        weightStatus = weightCategories.get(2)
    elif bodyMassIndex >= 30: # Obese
        weightStatus = weightCategories.get(3)
    else: # Catch out of bounds answer
        weightStatus = "Uncategorized"

    # Display BMI
    print("\nYour BMI is", bodyMassIndex, "and is in the", weightStatus, "category\n")

# Run the loop
runAgain = 'y'
while(runAgain == 'y'):
    getBMI()
    runAgain = input("Get entries for another person (y/n)? ")
