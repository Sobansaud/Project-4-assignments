SENTENCE_START: str = "Yesterday, I saw a "

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + " down the street. It was hilarious!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()