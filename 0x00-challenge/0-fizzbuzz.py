#!/usr/bin/python3

import sys

def fizzbuzz(n):
    """
    Fizzbuzz function prints number from 1 to n seprated by a space.

    - For multiples of three print "fizz" instead of the number and
    multiples of five print "buzz"

    -for numbers which are multiples of both three and five print
    "fizzbuzzz"
    """



    if n < 1:
        return

    tmp_result = []

    for i in range(1, n + 1):
       if i % 3 == 0:
           tmp_result.append("FizzBuzz")


       elif(i % 3) == 0 and (i % 5 == 0):
           tmp_result.append("FizzBuzz")

       elif(i % 5) == 0:
           tmp_result.append("Buzz")

       else:
           tmp_result.append(str(i))

    print(" ".join(tmp_result))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)



