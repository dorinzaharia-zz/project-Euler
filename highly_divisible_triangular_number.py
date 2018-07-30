import time

def main():
    """

    """
    start = time.time()

    num = 0
    i = 0
    number_of_divisor = 0
    N = 500

    while number_of_divisor < N:
        i += 1
        number_of_divisor = 0
        num = num + i

        for j in range(1, int(num**0.5)):
            if num % j == 0:
                number_of_divisor = number_of_divisor + 2

    print("Triangular number: " + str(num))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
