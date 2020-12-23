import matplotlib.pyplot as plt

from sum_digits_of_squared_naturals import sum_digits

from_power = 2
until_power = 100
start = 2
end = 3000
x_axis = []
y_axis = []

resulted_map_of_lists = {}


def run():
    for power in range(from_power, until_power + 1):
        # Initialize list for given power
        resulted_list = []
        for number in range(start, end + 1):
            # Sum digits
            calculated_powered_sum = power_num_and_sum_digits(number, power)
            # Compare sum of digits with actual number
            if calculated_powered_sum == number:
                # Add to resulted list
                resulted_list.append(calculated_powered_sum)
        # Add list as element of lists
        resulted_map_of_lists[power] = resulted_list

    # Print results
    for result_ in resulted_map_of_lists.items():
        print("Power {}".format(str(result_)
                                .replace(",", ":", 1)
                                .replace("(", "")
                                .replace(")", "")))


def power_num_and_sum_digits(value, power):
    num = pow(value, power)
    total = sum_digits(num)
    return total


def plot():
    plt.plot(x_axis, y_axis)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


run()
# plot()
