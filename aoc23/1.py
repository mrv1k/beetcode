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


test_input2 = ['1one',
               'six9',
               'fourtwo',
               '69',
               'qqqq6xxxx9xxxxxx',
               '4nineeightseven2',
               'eightwothree',
               ]

x = ['two1nine',
     'eightwothree',
     'abcone2threexyz',
     'xtwone3four',
     '4nineeightseven2',
     'zoneight234',  # 14 - one is valid, thus only ight is left
     '7pqrstsixteen']  # 76, no double digits support


# It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as
# valid "digits".
str_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'six': '6', 'six': '6',
            'seven': '7', 'eight': '8', 'nine': '9'}

# TODO: go through list and replace string digits with real digits


def day1part2():
    calibrations = []
    for raw_string in test_input2:
        # check raw_string for existence of string digits
        # if found replace
        string = raw_string
        # shitty sliding window to avoid having to learn with python regex
        start = 0
        end = 5

        for i in range(0, len(raw_string) + 1):
            slice = raw_string[start:end]
            # print(slice)
            found = False
            for str_num in str_nums:
                if str_num in slice:
                    string = string.replace(str_num, str_nums[str_num], 1)
                    start += len(str_num)
                    end = start + 5
                    # print(i, len(str_num), slice, str_num, start, end)
                    found = True
                    break

            if not found:
                start += 1
                end += 1

        print(raw_string, string)
        calibration = []
        for char in string:
            try:
                int(char)
                calibration.append(char)
            except ValueError:
                pass
        calibrations.append(calibration)

    sum = 0
    print(calibrations)
    for c in calibrations:
        first_and_last = int(c[0] + c[-1])
        print(first_and_last)
        sum += first_and_last

    return sum


print(day1part2())
