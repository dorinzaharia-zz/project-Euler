import time

def main():

    start = time.time()

    sequence_length = 0
    starting_number = 0
    sequence = 0

    for i in range(2, 1000000):
        length = 1
        sequence = i
        while sequence != 1:
            if sequence % 2 == 0:
                sequence /= 2
            else:
                sequence = sequence * 3 + 1
            length += 1
        if length > sequence_length:
            sequence_length = length
            starting_number = i

    print("Longest sequence: " + str(starting_number))

    finish = time.time()

    print("Execution time : " + str(finish - start))

if __name__ == "__main__":
    main()
