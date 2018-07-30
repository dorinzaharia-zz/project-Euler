import time

def main():

    start = time.time()

    file = open('one_hundred_50_digit_number.txt','r')

    list_of_int = []

    list_of_int = [int(line) for line in file]

    s = sum(list_of_int)

    string_sum = str(s)
    print(string_sum[:10])

    finish = time.time()
    print("Execution time: " + str(finish - start))

if __name__ == "__main__":
    main()
