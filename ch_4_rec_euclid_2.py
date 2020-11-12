# Implementing Euclidean Algorithm through modulo operator

def rec_euclid_2(a, b):
    """For simplicity: a must be greater than b"""
    if a % b == 0:
        return b

    return rec_euclid_2(b, a % b)


print(rec_euclid_2(12, 30))
print(rec_euclid_2(1680, 640))
