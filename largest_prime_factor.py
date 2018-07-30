import time


#check if number is prime
def is_prime(number):

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for iterator in range(3, int(number/2) + 1, 2):
        if number % iterator == 0:
            return False

    return True


def largest_number(number):

    divisor = 2
    largest_prime_number = 1

    while number > 1:
        if number % divisor == 0:
            number /= divisor
            if largest_prime_number < divisor and is_prime(divisor):
                largest_prime_number = divisor
            divisor = 2

        else:
            divisor +=1

    return largest_prime_number

def main():

    start = time.time()
    print("Largest prime number: " + str(largest_number(600851475143)))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
