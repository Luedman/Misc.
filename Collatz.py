from matplotlib import pyplot as plt
import numpy as np

number = int(input("Starting Number: "))

def collatz(number: int, plot=False):
    series = []
    odd_series = []
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            odd_series.append(int(number))
            number = 3*number + 1
        series.append(int(number))
    
    if plot:
        plt.plot(series)

    print(series)
    print(odd_series)
    print()

    return series, odd_series

series, odd_series = collatz(number)

def is_prime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                result = False
                break
            else:
                result = True
    else:
        pass

    return result

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

for num in odd_series:
    print(str(num) + "\t  " + str(primes(num)))
plt.plot(odd_series)
print()

for num in series:
    print(str(num) + "\t  " + str(primes(num)))
print()

try:
    plt.show()
except:
    pass