#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program uses while loops to add integers


def main():
    # This function uses while loops to add integers
    counter = 0
    sum = 0

    # Input
    integer_as_string = input("Input a positive integer: ")
    print("")

    # Process and Output
    try:
        integer_as_integer = int(integer_as_string)
        while counter < integer_as_integer:
            counter = counter + 1
            sum = sum + counter
        print(
            "The sum of all positive integers from 1 to {0} is {1}.".format(
                integer_as_string, sum
            )
        )

    except Exception:
        print("Please input a valid integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
