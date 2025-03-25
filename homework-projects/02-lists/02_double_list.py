def main():
    number_lists = [1,2,3,4,5,6,7,8,9,10]

    for index in range(len(number_lists)):
        elements = number_lists[index]
        number_lists[index] = elements * 2
        print(f" Element at index {index} is {number_lists[index]}")

if __name__ == "__main__":
    main()