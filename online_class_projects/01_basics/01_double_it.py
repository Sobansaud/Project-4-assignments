# Ask user to input a number
start_value = int(input("Enter a number: "))

# Set current value
curr_value = start_value

# Continue doubling until value is 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value)
