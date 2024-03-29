#!/usr/bin/env python3
# Lab 02 - Tyler Harrison

# display a welcome message
print("The Miles Per Gallon program")
print()
# get input from the user
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))
if (miles_driven <= 0) or (gallons_used <= 0):
    print("Miles and Gallons driven must be greater than zero. Try again.")
else: # calculate and display miles per gallon
    mpg = round((miles_driven/ gallons_used), 2)
    print("Miles Per Gallon:          ", mpg)
print()
print("Bye")