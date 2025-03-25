length = 5

def short(list):
    while len(list) > length:
        last_elem = list.pop()
        print(f"Removed {last_elem} from the list")

def get_list():
    list = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        list.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
        return list
    
def main():
    list = get_list()
    short(list)

if __name__ == "__main__":
    main()
