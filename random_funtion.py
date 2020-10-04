#! /usr/bin/python3

import random

def run():
    number_found = False
    random_number = random.randint(0, 20)
    print(random_number)

    while not number_found:
        number = int(input('Try a number: '))

        if number == random_number:
            print('Congratulations. You found the number!')
            number_found = True
        elif number > random_number:
            print('Sorry. Try a lower number')
        else:
            print('Sorry. Try a higher number')


if __name__ == '__main__':
    run()
