#!/usr/bin/env python3
print("Katlynn Davis Rectangle App")            # Welcome message

# display a welcome message
# print("The Miles Per Gallon program")
print()                                         # Print blank line

# get input from the user
length = float(input("Please enter the length:\t"))     # Prompt user for length input
width = float(input("Please enter the width:\t\t"))     # Prompt user for width input

# calculate area of a rectangle
area = round(length * width, 2)                 # Multiplies the length by the width, rounds results two decimal places

# calculate perimeter of a rectangle
perimeter = round(length * 2 + width * 2, 2)    # Multiplies length by 2 and width by 2 and then adds both together, rounds results two decimal places 
            
# format and display the result
print()                                         # Print's blank line
print("Area = \t\t\t" + str(area))              # Print's area
print("Perimeter = \t\t" + str(perimeter))      # Print's perimeter
print()                                         # Print's blank line
print("Thanks for using this program!")         # Print's Thanks for using this program!
