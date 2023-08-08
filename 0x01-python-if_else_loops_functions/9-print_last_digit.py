#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last_didit = number % 10
    print(last_didit, end="")
    return (last_didit)
