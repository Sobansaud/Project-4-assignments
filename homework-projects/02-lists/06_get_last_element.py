# Function to print the last element of the list
def get_last_element(lst):
    """ Prints the last element of the provided list. """
    print(lst[-1])  # The simpler way to access the last element

# Function to get the list from the user
def get_lst():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = []  # Start with an empty list
    elem = input("Please enter an element of the list or press enter to stop: ")  # Prompt user for input
    while elem != "":  # Keep asking for input until the user presses enter without typing anything
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Ask for the next element
    return lst  # Return the list of elements

# Main function where the program runs
def main():
    lst = get_lst()  # Get the list from the user
    get_last_element(lst)  # Print the last element of the list

# Start the program
if __name__ == '__main__':
    main()
