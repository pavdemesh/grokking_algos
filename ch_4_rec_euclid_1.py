# Implementing Euclidean Algorithm through subtraction

def rec_euclid_1(a, b):
    """The function will subtract lesser number from the larger until they are equal"""
    if a == b:
        return a

    if a > b:
        return rec_euclid_1(a - b, b)

    else:
        return rec_euclid_1(b - a, a)


print(rec_euclid_1(12, 30))
print(rec_euclid_1(1680, 640))
