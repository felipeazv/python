import math

start = 1
end = 100


##
## s = (1!/1)+(2!/2^2)+(3!+3^3)+(4!+4^4)+...+(n!/n^n)
## s = [1,∞]Σ(x!/x^x)
##

def sum_of_factorials_divided_by_powers():
    partial_sum = 0
    for number in range(start, end + 1):
        factorial = math.factorial(number)
        power = math.pow(number, number)
        partial_sum += factorial / power
        print(partial_sum)


sum_of_factorials_divided_by_powers()


## Prove that lim[a→∞]∑[n=1,∞] (n!^a)/(n^an)=1.
def sum_term(n, a):
    return (pow(math.factorial(n), a)) / pow(n, a * n)


def apply_sum_term():
    for a in range(1, 21):
        value = 0
        for n in range(1, 1001):
            value += sum_term(n, a)
        print("a = " + str(a) + " | lim = " + str(value))
