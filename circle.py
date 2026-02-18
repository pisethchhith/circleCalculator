# Circle_calculator

# first, give user prompt the value of radius, and diameter in meter
# if user prompt beside of meter, convert to meter
# then calculates Area of circle


# thing I want to change
    # the interaction
        # loop only user selected
    # complex unit (not only m^2)

import sys
import time

length_unit = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

def circleCalculator():
    title = "Hello, Welcome to circle Calculator"
    animation(title)
    print()
    while True:
        try:
            print("""What would you like to calculate Area of Circle with?
1.Radius
2.Diameter
3.Options
4.Quit""")
            user = input("Enter the number: ")
            process = "Processing......."
            if user == "1":
                radius = input("Radius: ")
                animation(process)
                print(f"Area: {radiusCalculation(radius)} m^2\n")
                time.sleep(2)
            elif user == "2":
                diameter = input("Diameter: ")
                animation(process)
                print(f"Area: {diameterCalculation(diameter)} m^2\n")
                time.sleep(2)
            elif user == "4":
                close = "Goodbye, hoping to see you again :)"
                animation(close)
                sys.exit()
        
        except (ValueError):
            pass

def radiusCalculation(Radius):
    number, unit = Radius.split(" ")
    PI = 3.14
    if unit in length_unit[0:2]:
        radius = UnitConversion(number, unit)
    elif unit in length_unit[-3:]:
        radius = UnitConversion(number, unit)
    elif unit in length_unit[3]:
        radius = float(number)
    
    return 2 * PI * pow(radius, 2)
            
def diameterCalculation(Diameter):
    number, unit = Diameter.split(" ")
    PI = 3.14
    if unit in length_unit[0:2]:
        diameter = UnitConversion(number, unit)
    elif unit in length_unit[4:6]:
        diameter = UnitConversion(number, unit)
    elif unit in length_unit[3]:
        diameter = float(number)
   
    return (PI/4) * pow(diameter, 2)


def UnitConversion(Number, Unit): # convert all unit to meter
    try:
        if Unit in length_unit[0]:
            return float(Number) * 1000
        elif Unit in length_unit[1]:
            return float(Number) * 100
        elif Unit in length_unit[2]:
            return float(Number) * 10
        elif Unit in length_unit[-3]:
            return float(Number) / 10
        elif Unit in length_unit[-2]:
            return float(Number) / 100
        elif Unit in length_unit[-1]:
            return float(Number) / 1000
    except UnboundLocalError:
        raise ValueError

def animation(Title):
    for character in Title:
        time.sleep(0.1)
        sys.stdout.write(character)
        sys.stdout.flush()
    time.sleep(1)
    print()
    

if __name__ == "__main__":
    circleCalculator()

