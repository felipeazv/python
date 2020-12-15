from sum_digits_of_squared_naturals import sum_digits, math

pwr = 3
start = 3
end = 100
x_axis = []
y_axis = []

iterations = 0


def run():
    global iterations
    for number in range(start, end):
        iterations += 1
        # calculated_cubed_sum = 3 if number % 3 == 0 else cube_and_sum_digits(number)
        calculated_cubed_sum = cube_and_sum_digits(number)

        # print("{} sum of cubed number {} with and {} iterations".format(number, calculated_cubed_sum, iterations))
        if calculated_cubed_sum == number:
            print("!!!!{} {}".format(number, calculated_cubed_sum))

        iterations = 0


def cube_and_sum_digits(value):
    num = pow(value, pwr)
    total = sum_digits(num)
    # if iterate_again(total):
    #     total = cube_and_sum_digits(total)

    return total


def iterate_again(value):
    global iterations

    if value == 1:
        return False
    # Infinite loop => 17³ = 4913 => sum digits => 17
    if value == 8:
        return False
    # Infinite loop => 17³ = 4913 => sum digits => 17
    if value == 17:
        return False
    # Infinite loop => 19³ = 6859 => sum digits => 28 => 28³ => 21952 => sum digits = 19
    if value == 19:
        return False
    # Infinite loop => 19³ = 6859 => sum digits => 28 => 28³ => 21952 => sum digits = 19
    if value == 19:
        return False

    iterations += 1
    return True


run()

