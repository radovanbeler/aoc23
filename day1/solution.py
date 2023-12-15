import re

FILE = 'day1/input.txt'

with open(FILE, encoding='utf8') as file:
    lines = file.readlines()

calibration_values = []
for line in lines:
    numbers = [c for c in line if c.isdigit()]
    calibration_values.append(int(numbers[0] + numbers[-1]))

print(f"First part: {sum(calibration_values)}")

num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def to_num(number):
    if number.isdigit():
        return number

    return num_map[number]

p = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
calibration_values = []
for line in lines:
    numbers = p.findall(line)
    value = int(to_num(numbers[0]) + to_num(numbers[-1]))
    calibration_values.append(value)

print(f"Second part: {sum(calibration_values)}")

