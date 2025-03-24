def main():
    print("Convert Fahrenheit to Celsius")

    fahrenheit = float(input("Enter the temperature in Fahrenheit :"))

    celsius = (fahrenheit - 32) * 5.0/9.0

    print(f"The temperature is {fahrenheit} °F is convert to {celsius}°C")

if __name__ == "__main__":
    main()
