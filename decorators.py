#! /usr/bin/python3

def funtion_decorator(funtion_parameter):

    def funtion_interior():
        # addind a decorate
        print("let's calculate: ")
        funtion_parameter()
        # adding a decorate
        print("end of calculate")
    return funtion_interior  # Important! only return without '()'


@funtion_decorator
def sum_2_numbers():
    print(15+20)


@funtion_decorator
def subtraction_2_numbers():
    print(30-10)


if __name__ == '__main__':
    sum_2_numbers()
    subtraction_2_numbers()
