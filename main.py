from time import perf_counter


def timed(fn):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print("Time taken: {0:.6f} secs".format(end - start))
        return result

    return inner


def get_user_input():
    while True:
        snum = input("Enter number: ")
        try:
            num = int(snum)
            return num
        except ValueError:
            print("Enter a valid number")
            continue


def recurion_fibonacci(num):
    if num <= 2:
        return 1
    else:
        return recurion_fibonacci(num - 2) + recurion_fibonacci(num - 1)

@timed
def calc_recurion_fibonacci(num):
    return recurion_fibonacci(num)

@timed
def loop_fibonacci(num):
    num1 = 1
    num2 = 1
    for i in range(3, num + 1):
        num1, num2 = num2, num1 + num2
    return num2


if __name__ == "__main__":
    num = get_user_input()
    print("Calculating Fibonacci for number : {0}".format(num))

    # recursion method
    #feb = calc_recurion_fibonacci(num)

    # using loop
    feb = loop_fibonacci(num)

    print("{0}th Fibonacci number is: {1}".format(num, feb))
