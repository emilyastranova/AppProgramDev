#!/usr/bin/env python3

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

outfile = open("trips.csv", "w")
def save_values(miles, gallons, mpg):
    outfile.write(str(miles) + "," + str(gallons) + "," + str(mpg) + "\n")

def main():
    outfile.write("Distance,Gallons,MPG\n")
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)
        save_values(miles_driven, gallons_used, mpg)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye")
    outfile.close()

if __name__ == "__main__":
    main()

