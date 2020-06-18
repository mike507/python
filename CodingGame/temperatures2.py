import sys

if __name__ == "__main__":
    # the number of temperatures to analyse
    n = int(input())
    if n == 0:
        min_temperature = 0
    else:
        min_temperature = 5526
    temperatures = [int(t) for t in input().split()]
    calc = lambda t, mt: t if any([abs(t) < abs(mt), abs(t) == abs(mt) and t > 0]) else mt
    for t in temperatures:
        min_temperature = calc(t, min_temperature)

    print(min_temperature)


