import logging
logging.basicConfig(filename="EvenOddnumber.py", filemode="w")
def even_Odd(number):
    """
    :param number:
    :return:
    """
    if number % 2 == 0:
        return True
    return False

if __name__=="__main__":
    try:
        number = int(input("Enter a integer number"))
        if even_Odd(number)==True:
            print("Number is Even")
        else:
            print("Number is odd")
    except:
        print("Enter valid number")
