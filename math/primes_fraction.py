from sum_digits_of_squared_naturals import is_prime

import matplotlib.pyplot as plt

x_axis = []
y_axis = []

fList = []
start = 1
end = 1000


def primes():
    count = 0
    for number in range(start, end + 1):
        if is_prime(number):
            fList.append(number)
            count = count + 1
            if count > 2:
                val1 = fList[count - 1]
                val2 = fList[count - 2]
                fraction = val1 / val2
                print(fraction)
                x_axis.append(count)
                y_axis.append(fraction)

    # print(fList)


def plot():
    plt.plot(x_axis, y_axis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


primes()
# plot()
