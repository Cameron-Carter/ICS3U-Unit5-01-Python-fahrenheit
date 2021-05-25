#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program converts temperature in degrees Celsius to Fahrenheit

import random
import string


def convert_to_fahrenheit():
    # Convert to fahrenheit

    # Input
    celsius_as_string = str(input(
        "Enter the temperature in degrees Celsius: "
    ))

    # Process and output
    try:
        celsius_as_float = float(celsius_as_string)
        fahrenheit = (9 / 5) * celsius_as_float + 32
        print("The temperature in degrees Fahrenheit is {}°.".format(fahrenheit))
    except Exception:
        print("Invalid temperature!")
    finally:
        print("\nDone.")


def main():
    # This function calls fahrenheit

    # Call fahrenheit
    convert_to_fahrenheit()


if __name__ == "__main__":
    main()
