#! /usr/bin/python3

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(input('Write a number: '))
    result = factorial(number)
    print()
    print('The factorial of {} is {}'.format(number, result))