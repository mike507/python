import sys

if __name__ == "__main__":
    # the number of temperatures to analyse
    n = int(input())
    if n == 0:
        min_temperature = 0
    else:
        min_temperature = 5526

    for t in input().split():
        temperature = int(t)
        if any([
            abs(temperature) < abs(min_temperature),
            abs(temperature) == abs(min_temperature) and temperature > 0
        ]):
            min_temperature = temperature

    print(min_temperature)

