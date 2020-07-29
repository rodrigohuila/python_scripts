# This is a guest the number game
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20. ')
secretNumber = random.randint(1, 20)

#print('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print ('\nTake a guess.')
    guess = int(input())

    if guess < secretNumber:
        print ('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!        
    
if guess == secretNumber:
    print('\n Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses! ')
else:
    print('\n Nope, The number I was thinking of was ' + str(secretNumber))



# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input('Elige un número del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print('Busca un número más grande')
#         else:
#             print('Busca un número más pequeño')
#         numero_elegido = int(input('Elige otro número: '))
#     print('¡Ganaste!')


#if __name__ == '__main__':
#    run()
