import time

def main():

    start = time.time()
    
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                print("Largest product: " + str(a * b * c))
                break

    finish = time.time()
    print("Execution time : " + str(finish - start))

if __name__ == '__main__':
    main()
