#!/usr/bin/env python3

print("Katlynn Davis MPG App") # Welcome message
# display a welcome message
# print("The Miles Per Gallon program")
print()                       # Print blank line

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))           # Promt user for miles driven input
gallons_used = float(input("Enter gallons of gas used:\t"))     # Prompt user for gallons of gas used input
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))    # Promt user for cost per gallon input

# calculate miles per gallon
# mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)

# Calculate total gas cost
total_gas_cost = round(miles_driven / mpg * cost_per_gallon, 2)

#Calculate cost per mile
cost_per_mile = round(total_gas_cost / miles_driven, 2)
            
# format and display the result
print()                                                 # Print blank line
print("Miles Per Gallon:\t\t" + str(mpg))               # Displays miles per gallon
print("Total gas cost:\t\t\t" + str(total_gas_cost))    # Displays total gas cost
print("Cost per mile:\t\t\t" + str(cost_per_mile))      # Displays cost per mile
print()                                                 # Print blank line
print("Bye")                                            # Print Bye
