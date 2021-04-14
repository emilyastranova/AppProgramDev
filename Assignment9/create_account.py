#!/usr/bin/env python3

fullName = input("Enter full name:        ")
password = input("Enter password:         ")

while True:
    emailAddress = input("Enter email address:    ")    # Must have @ and .com
    if emailAddress.find("@") >=0 and emailAddress.find(".com") >= 0:
        break
    else:
        print("Please enter a valid email address.")

while True:
    phoneNumber = input("Enter phone number:     ")     # Must have 10 digits, strip away (), -, and whitespace
    phoneNumber = phoneNumber.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    if phoneNumber.isdigit() and len(phoneNumber) == 10:
        break
    else:
        print("Please enter a 10-digit phone number. ")