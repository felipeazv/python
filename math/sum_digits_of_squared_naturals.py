import math
import matplotlib.pyplot as plt

pwr = 2
start = 4
end = 100000000000000984875

iterations = 0
x_axis = []
y_axis = []


def run():
    global x_axis
    global y_axis
    global iterations
    for number in range(start, end):
        iterations += 1
        calculated_squared_sum = 3 if number % 3 == 0 else square_and_sum_digits(number)
        ok = calculated_squared_sum == 1 or is_prime(calculated_squared_sum)

        if not ok:
            print("{} generates {}, which is not prime".format(number, calculated_squared_sum))
            break

        # print("{} value of {} with a total of {} iterations".format(number, calculated_squared_sum, iterations))
        # x_axis.append(number)
        # y_axis.append(calculated_squared_sum)
        iterations = 0


def iterate_again(value):
    global iterations

    if value == 1:
        return False
    if value % 2 == 0 or value % 5 == 0 or math.sqrt(value) * math.sqrt(value) == value:
        iterations += 1
        return True
    return False


def sum_digits(num):
    sum_of_digits = 0
    while num > 0:
        dig = num % 10
        sum_of_digits += dig
        num = num // 10
    return sum_of_digits


def square_and_sum_digits(value):
    num = pow(value, pwr)
    total = sum_digits(num)
    if iterate_again(total):
        total = square_and_sum_digits(total)

    return total


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def plot():
    # # plt.ylim([1, 23])
    plt.scatter(x_axis, y_axis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


run()
# plot()
