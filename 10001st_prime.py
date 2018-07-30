import time

def is_prime(number):

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number / 2) + 1, 2):
        if number % i == 0:
            return False

    return True

def main():

    """
    Cheking every odd number if is prime and increment count to calculate n-st prime
    """

    start = time.time()

    count = 1
    number = 1
    N = 10001


    while count < N:
        number += 2
        if is_prime(number):
            count += 1

    print(str(N) + "st prime: " + str(number))

    finish = time.time()
    print("Execution time: " + str(finish - start))

if __name__ == "__main__":
    main()
