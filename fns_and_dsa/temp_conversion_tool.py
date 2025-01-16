# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

