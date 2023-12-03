# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

calibration_list = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

calibrations = []
for s in calibration_list:
    calibration = []
    for c in s:
        try:
            d = int(c)
            calibration.append(c)
        except ValueError:
            pass
    calibrations.append(calibration)
print(calibrations)

result = 0
for c in calibrations:
    first_and_last = int(c[0] + c[-1])
    result = result + first_and_last


assert result == 142, 'incorrect result'
print(result)
