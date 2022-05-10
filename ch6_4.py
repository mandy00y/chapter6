

def power(r, n):
    if n == 1:
        return r
    else:
        return r * power(r, n - 1)

print("result", power(2, 3))
# the ouput is the answer to 2 to the 3rd power = 2 * 2 * 2 = 8



def power_2(r, n):
    value = 1
    for i in range(1, n + 1):
        value = r * value
    return value

print(power(3, 3))
# output will be 27 = 3 * 3 * 3
# the coding on top ===========> work as well


