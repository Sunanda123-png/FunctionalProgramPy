import logging
logging.basicConfig(filename="SwapNumber.py", filemode="w")
def swap_numbers(num1, num2):
    """
    :param num1:
    :param num2:
    :return:
    """
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping, number1 is %d and number2 is %d"% (num1, num2))

if __name__ == '__main__':
    try:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print("Before swapping, number1 is %d and number2 is %d"% (num1, num2))
        swap_numbers(num1, num2)
    except:
        print("Enter valid number")

