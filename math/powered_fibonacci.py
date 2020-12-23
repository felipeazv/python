import matplotlib.pyplot as plt

x_axis = []
y_axis = []

fList = []
start = 1
end = 30
count = 0


# fibonacci: 1.6180339887543225
# cubed fib:
def powered_fib(power):
    fList.append(start)
    count = 1
    for _ in range(start, end):
        if count < 2:
            fList.append(1)
        else:
            val1 = pow(fList[count - 1], power)
            val2 = pow(fList[count - 2], power)
            next_value = val2 + val1
            fList.append(next_value)
            fraction = val1 / val2
            # x_axis.append(count)
            # y_axis.append(fraction)
            print(fraction)

        count = count + 1

    print(fList, end=' ')


# fibonacci: 1.618033988749895


def plot():
    plt.plot(x_axis, y_axis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


# original
powered_fib(1)
# powered_fib(2)
print("---")
# powered_fib(3)
print("---")
# powered_fib(4)
# plot()
