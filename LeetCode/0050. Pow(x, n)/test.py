from math import log2, floor


def base_10_to_binary_array(n):
    if n == 0:
        return [0]
    powers = floor(log2(n))
    bit_array = [0] * (powers + 1)
    power_2 = 1
    for _ in range(powers):
        power_2 *= 2
    for i in range(powers, -1, -1):
        bit_array[powers - i], n = divmod(n, power_2)
        power_2 = power_2 // 2
    return bit_array

for i in range(20):
    print(i, base_10_to_binary_array(i))
