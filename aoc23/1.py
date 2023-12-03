# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

# input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
input = open('./input/1.txt', 'r')


def day1part1():
    calibrations = []
    for string in input:
        calibration = []
        for char in string:
            try:
                int(char)
                calibration.append(char)
            except ValueError:
                pass
        calibrations.append(calibration)

    sum = 0
    for c in calibrations:
        first_and_last = int(c[0] + c[-1])
        sum += first_and_last

    return sum


print(day1part1())


def day1part2():
    calibrations = []
    for string in input:
        calibration = []
        for char in string:
            try:
                int(char)
                calibration.append(char)
            except ValueError:
                pass
        calibrations.append(calibration)

    sum = 0
    for c in calibrations:
        first_and_last = int(c[0] + c[-1])
        sum += first_and_last

    return sum
