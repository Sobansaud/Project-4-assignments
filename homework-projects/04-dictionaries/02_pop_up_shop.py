def main():
    fruits = {
        "apple" : 1.5,
        "durian" : 50,
        'jackfruit': 80,
          'kiwi': 1, 
          'rambutan': 1.5,
         'mango': 5
    }

    total_cost = 0
    for fruits_name in fruits:
        price = fruits[fruits_name]
        bought = int(input(f"How many {fruits_name} do you want to buy? "))
        total_cost += price * bought
        print(" You have bought", bought, fruits_name, "for", price * bought)

if __name__ == "__main__":
    main()