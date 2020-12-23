import matplotlib.pyplot as plt

x_axis = []
y_axis = []

fList = []
start = 1
end = 20


# 1.324717957244746 100 iterations
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, (Nk-2 + Nk-3), where N
def padovan_sequence():
    fList.append(start)
    print(fList[0], end=' ')
    count = 1
    for _ in range(start, end):
        # for _ in fList:
        if count <= 2:
            fList.append(1)
            print(fList[count], end=' ')
        else:
            if 2 < count <= 4:
                fList.append(2)
                print(fList[count], end=' ')
            else:
                fList.append(fList[count - 2] + fList[count - 3])
                fraction = fList[count - 2] / fList[count - 3]
                # x_axis.append(count)
                # y_axis.append(fraction)
                print(fList[count], end=' ')

                # print(fraction)

        count = count + 1


def plot():
    plt.plot(x_axis, y_axis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


padovan_sequence()
plot()
