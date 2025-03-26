import random

numbers = 10
min = 1
max = 100

def main():
    for _ in range(numbers):
        print(random.randint(min,max) , end= "")

if __name__ == "__main__":
    main()