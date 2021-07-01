def text_analyser(text : str, *args):
    """text_analyser(text : str):
        Parameters:
            text (str): text you want to be analysed
        prints various informations about text passed as argument:
        number of lowercase letter, number of uppercase letters, number of spaces, number of punctuation characters
    """
    if (len(args)):
        print("ERROR")
        return
    lowerCount = 0
    upperCount = 0
    punctCount = 0
    spaceCount = 0

    for c in text:
        if (c.isupper()):
            upperCount += 1
        elif (c.islower()):
            lowerCount += 1
        elif (c.isspace()):
            spaceCount += 1
        elif (c.isprintable() and not c.isalnum()):
            punctCount += 1
    print(text)
    print("- ", upperCount," upper letters")
    print("- ", lowerCount," lower letters")
    print("- ", spaceCount," spaces")
    print("- ", punctCount," punctuation marks")
    