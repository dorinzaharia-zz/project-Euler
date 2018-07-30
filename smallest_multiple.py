import time

def is_prime(number):

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number/2) + 1, 2):
        if number % i == 0:
            return False

    return True


def smallest_multiple():
"""
To calculate smallest number which is evenly divisible by all of the numbers from 1 to 20
is enough to calculate multiple of all prime numbers raised
to a maximal power in which this number is smaller than our range
"""

#list to store power of numbers
    array_of_exponents = list()

    for i in range(2, 20):
        array_of_exponents.append(1)
        if is_prime(i):
            nr = i
            #calculating max power
            while nr*i < 20:
                array_of_exponents[i-2] += 1
                nr *= i

    multiple = 1

    for i in range(2, 20):
        if is_prime(i):
            multiple *= pow(i, array_of_exponents[i-2])

    return multiple


def main():

    start = time.time()

    print("Smallest multiple: " + str(smallest_multiple()))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
