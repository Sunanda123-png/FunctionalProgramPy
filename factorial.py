import math
if __name__=="__main__":
    try:
        num = int(input("Enter a number: "))
        print(math.factorial(num))
    except:
        print("Enter a number")
