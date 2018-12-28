####
# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number.  
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
import argparse
import sys

parser = argparse.ArgumentParser(
    description='This is a fizzbuzz program'
)

parser.add_argument(
    '--max',
    help='High celing of FizzBuzz'
)

args = parser.parse_args()


def main():
    n = int(sys.argv[2])
    for i in range(1, n+1):

        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__== "__main__":
    main()