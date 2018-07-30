import time

def is_prime(n):

    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():

    start = time.time()

    sum = 5

    for i in range(5, 2000000, 2):
        if is_prime(i):
            sum += i

    print("Sum: " + str(sum))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
