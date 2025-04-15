#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 14, 2025
# This program catches erroneous input
# and calculates the factorial of the user's
# input


def main():
    # Initializations
    counter = 0
    product = 1

    # Get the user's number
    num_string = input("Enter your number: ")

    # CAST the string into an integer
    try:
        num_integer = int(num_string)
        if num_integer < 0:
            print("{} should be bigger than 0".format(num_integer))
        else:
            while True:
                counter = counter + 1
                product = counter * counter
                print("Tracking {} times through loop".format(counter))
                if counter >= num_integer:
                    break
            print("{}! = {}".format(num_integer, product))

    except Exception:
        print("{} is not a valid number".format(num_string))


if __name__ == "__main__":
    main()
