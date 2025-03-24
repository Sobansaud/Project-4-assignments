c = 299792458  # The speed of light in m/s

def main():
    mass_kg = float(input("Enter the mass of the object in kg : "))

    energy_joule = mass_kg * c**2

    print("The energy of the object is : ", energy_joule, "J")
    print("The mass of the object is : ", mass_kg, "kg")
    print("The Speed of light is : ", c, "m/s")

if __name__ == "__main__":
    main()

