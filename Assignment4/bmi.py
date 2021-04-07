#!/usr/bin/env python3
# Enhanced BMI Calculator Lab - Tyler Harrison

import validation

def bmi_calculator(height, weight):

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
    return str("\nYour BMI is " + str(round(bodyMassIndex)) + " and is in the " + str(weightStatus) + " category\n")

def main():
    print("The Body Mass Index Calculator\n")
    # Run the loop
    runAgain = 'y'
    while(runAgain.lower() == 'y'):
        # Get user input
        height = validation.get_int("Enter height (in inches): ", 55, 83)
        weight = validation.get_float("Enter weight (in lbs): ", 90, 290)
        print(bmi_calculator(height, weight))
        runAgain = input("Get entries for another person (y/n)? ")

if __name__ == "__main__":
    main()