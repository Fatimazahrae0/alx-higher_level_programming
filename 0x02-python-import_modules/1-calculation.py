#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum = add(a, b)
    min = sub(a, b)
    mlt = mul(a, b)
    dvs = div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, min))
    print("{} * {} = {}".format(a, b, mlt))
    print("{} / {} = {}".format(a, b, dvs))
