def fibonacci_series(limit):
    """
    :param limit:
    :return:
    """
    a, b = 0, 1
    while a < limit:
        print(a, end=' ')
        a, b = b, a + b
    print()


if __name__ == "__main__":
    try:
        limit = float(input("Enter number of terms: "))
        fibonacci_series(limit)

    except Exception as e:
        print("Enter valid input")
