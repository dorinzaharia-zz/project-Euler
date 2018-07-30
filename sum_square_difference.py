import time

def main():

    start = time.time()

    n = 100

    #sum of the squares of first n number s= (n * (n+1) * (2 * n + 1)) /6
    sum_of_squares = (n*(n + 1)*(2*n + 1))/6

    #sum of first n numbers s= n * ( n + 1) / 2
    square_of_sum = pow(n*(n + 1)/2, 2)

    print("Difference: " + str(square_of_sum - sum_of_squares))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
