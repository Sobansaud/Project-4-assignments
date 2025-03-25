def three_copy(lists, data):
    for i in range(3):
        lists.append(data)

def main():
    message = input(" Enter a message to copy three times : ")
    lists = []
    print("Lists before " , lists)
    three_copy(lists,message)
    print("After Lists " , lists)

if __name__ == "__main__":
    main()