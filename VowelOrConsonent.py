def vowel(character):
    if (character == 'A' or character == 'a' or character == 'E' or character == 'e' or character == 'I'
            or character == 'i' or character == 'O' or character == 'o' or character == 'U' or character == 'u'):
        return True

    return False

if __name__ == "__main__":
    character = input("Enter a character: ")
    if vowel(character) == True:
        print("This is vowel")
    else:
        print("This is consonent")
