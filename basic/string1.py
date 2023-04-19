#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Базові вправи з рядками
# Заповніть код функцій нижче. main() вже налаштовано
# для виклику функцій з декількома різними вхідними даними,
# виводячи 'OK', коли кожна функція працює коректно.
# Початковий код кожної функції включає 'return'
# який є лише заповнювачем для вашого коду.
# Нічого страшного, якщо ви не завершите всі функції, і є
# у string2.py є додаткові функції, які варто спробувати.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    if count < 10:
        return f'Number of donuts: {count}'
    else:
        return 'Number of donuts: many'


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#
def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' Pass '
    else:
        prefix = ' Not pass '
    return f'{prefix}, {repr(got)}, {repr(expected)}'


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.

def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    print(test(donuts(4), 'Number of donuts: 4'))
    print(test(donuts(9), 'Number of donuts: 9'))
    print(test(donuts(10), 'Number of donuts: many'))
    print(test(donuts(99), 'Number of donuts: many'))

    print('both_ends')
    print(test(both_ends('spring'), 'spng'))
    print(test(both_ends('Hello'), 'Helo'))
    print(test(both_ends('a'), ''))
    print(test(both_ends('xyz'), 'xyyz'))

    print('fix_start')
    print(test(fix_start('babble'), 'ba**le'))
    print(test(fix_start('aardvark'), 'a*rdv*rk'))
    print(test(fix_start('google'), 'goo*le'))
    print(test(fix_start('donut'), 'donut'))

    print('mix_up')
    print(test(mix_up('mix', 'pod'), 'pox mid'))
    print(test(mix_up('dog', 'dinner'), 'dig donner'))
    print(test(mix_up('gnash', 'sport'), 'spash gnort'))
    print(test(mix_up('pezzy', 'firm'), 'fizzy perm'))


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
