def vowel(ch):
    if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'
            or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        return True

    return False

if __name__ == "__main__":
    ch = input("Enter a character: ")
    if vowel(ch) == True:
        print("This is vowel")
    else:
        print("This is consonent")