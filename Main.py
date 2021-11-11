# The Josephus Problem Calculator
# https://www.ucd.ie/mathstat/t4media/1.%20The%20Josephus%20problem.pdf
# github.com/ex1tt

import math


class Math:

    @staticmethod
    def find_power(s):
        return 0 if s == 0 else 2 ** math.floor(math.log2(s))  # s = Number Of Soldiers

    @staticmethod
    def find_survivor(s):
        return (s - Math.find_power(s)) * 2 + 1  # s = Number Of Soldiers


print('The Josephus Problem Calculator')
print('https://www.ucd.ie/mathstat/t4media/1.%20The%20Josephus%20problem.pdf')
no_of_soldiers = int(input('\nEnter Number Of Soldiers: '))
print('')
print(Math.find_survivor(no_of_soldiers))
