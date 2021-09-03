def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')
    print()

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    print('Go ahead and enter 3 numbers: ')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")
    print()

def count():
    print('Now I will prove to you that I can count to any number you want.')
    print('Input a number: ')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's challenge your programming knowledge.")
    print("Why do we use methods?")
    print()
    print('1. To repeat a statement multiple times')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    number = int(input('Choose a number please: '))
    if number != 2:
        print('Please, try again.')
        print()
        test()
    else:
        print('Way to go!!! You have completed the challenge, have a nice day!')
    print()

def end():
    print('Thanks for your time, have a nice day!')


greet('John', '1985')
remind_name()
guess_age()
count()
test()
end()
