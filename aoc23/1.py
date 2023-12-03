# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

input1 = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
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


input3 = ['eighthree', 'sevenine'] # 83 79

input2 = [
    'two1nine',
    'eightwothree',  # 823, yes they can fucking overlap :(
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',  # 14 - one is valid, thus only ight is left
    '7pqrstsixteen']  # 76, no double digits support


# It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as
# valid "digits".
str_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6',  # 'six': '6', 'six': '6',
            'seven': '7', 'eight': '8', 'nine': '9'}

# TODO: go through list and replace string digits with real digits


def day1part2():
    calibrations = []
    for raw_string in input:
        string = ''
        start = 0
        end = 5
        while start < len(raw_string):
            slice = raw_string[start:end]
            found = False
            for str_num in str_nums:
                if str_num in slice:
                    string += slice.replace(str_num, str_nums[str_num])
                    start += len(str_num) - 1
                    end = start + 5
                    found = True
                    break

            if not found:
                string += raw_string[start]
                start += 1
                end += 1

        calibration = []
        for char in string:
            try:
                int(char)
                calibration.append(char)
            except ValueError:
                pass
        calibrations.append(calibration)
        c = calibration

    sum = 0
    for c in calibrations:
        first_and_last = int(c[0] + c[-1])
        sum += first_and_last

    return sum


print(day1part2())
