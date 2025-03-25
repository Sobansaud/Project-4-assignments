def main():
    list = []


    value = input("Enter a value : ")
    while value :
        list.append(value)
        value = input("Enter a value : ")
        print("The list is : ", list)

if __name__ == "__main__":
    main()