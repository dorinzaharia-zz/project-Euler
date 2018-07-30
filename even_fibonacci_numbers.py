import time

def calculate_fibonacci():

    first_number = 1
    second_number = 1

    """
    Every third Fibonacci term is even
    By adding two previous odd terms from Fibonacci sequence we recieve even term
    """

    #generator for even fibonacci numbers
    while True:
        yield first_number + second_number
        temp = first_number
        first_number = first_number + 2*second_number
        second_number = 2*temp + 3*second_number

def main():

    start = time.time()

    N = 4000000

    fibonacci_number = calculate_fibonacci()

    number = next(fibonacci_number)

    sum = 0

    while number < N:
        sum += number
        number = next(fibonacci_number)

    print("Sum = " + str(sum))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
