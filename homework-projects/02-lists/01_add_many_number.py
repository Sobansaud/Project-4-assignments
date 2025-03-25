def add_number(list_of_numbers):
    """This function takes a list of numbers and returns the sum of all numbers in the list."""

    total = 0
    for number in list_of_numbers:
        total += number

    return total

def main():
    lists_of_numbers = [1,2,5,6,7]
    sum_of_numbers = add_number(lists_of_numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()