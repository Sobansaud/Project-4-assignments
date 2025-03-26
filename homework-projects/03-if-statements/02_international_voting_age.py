Peturksbouipo = 16
Stanlau = 25
Mayengua  = 28

def main():
    user = int(input("How old are you? "))

    if user >= Peturksbouipo:
        print("You can vote in Peturksbouipo where voting age is ", Peturksbouipo, "years old")
    else:
        print("You can't vote in Peturksbouipo where voting age is ", Peturksbouipo, "years old")

    if user >= Stanlau:
        print("You can vote in Stanlau where voting age is ", Stanlau, "years old")
    else:
        print("You cannot vote in Stanlau where voting age is", Stanlau, "years old")

    if user >= Mayengua:
        print("You can vote in Mayengua where voting age is ", Mayengua, "years old")
    else:
        print("You cannot vote in Mayengua where voting age is", Mayengua, "years old")

if __name__ == "__main__":
    main()
