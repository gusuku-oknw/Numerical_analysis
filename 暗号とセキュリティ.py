import math

for k in range(1, 70):
    result = 1 - (math.factorial(365) / (365 ** k * math.factorial(365 - k)))
    print("{}人：確率{}".format(k, result))
