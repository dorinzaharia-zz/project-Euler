import time

def main():

    start = time.time()

    sum = 0
    iterator = 1

    for iterator in range(1000):
        if iterator % 3 == 0 or iterator % 5 == 0:
            sum += iterator

    print("Sum = " + str(sum))

    finish = time.time()

    print("Execution time : " + str(finish - start))
    
if __name__ == "__main__":
    main()
