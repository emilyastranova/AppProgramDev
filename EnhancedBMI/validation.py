#!/usr/bin/env python3

def get_float(prompt, low, high):
    userInput = float(input(prompt))
    while (userInput < low or userInput > high):
        userInput = float(input("Entry must be greater than " + str(low) + " and less than or equal to " + str(high) + "\n" + prompt))
    return userInput

def get_int(prompt, low, high):
    userInput = int(input(prompt))
    while (userInput < low or userInput > high):
        userInput = int(input("Entry must be greater than " + str(low) + " and less than or equal to " + str(high) + "\n" + prompt))
    return userInput

def main():
    choice = 'y'
    while(choice.lower() == 'y'):
        print(get_float("Insert float: ", 0.0, 10.0))
        print(get_int("Insert integer: ", 0.0, 10.0))
        choice = input("Do you want to continute? (Y/N): ")
        
if __name__ == "__main__":
    main()
