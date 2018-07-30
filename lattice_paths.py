import time
import math

def main():

    start = time.time()

    n_fact = math.factorial(20)

    nr = math.factorial(2 * 20) / n_fact / n_fact

    print(nr)


    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
