import re

FILE = 'day2/input.txt'

with open(FILE, encoding='utf8') as file:
    lines = file.readlines()

power_sum = 0
for line in lines:
    draws = re.findall(r"(\d+ \w+)", line)
    red_max, green_max, blue_max = 0, 0, 0
    for draw in draws:
        count, color = draw.split()
        count = int(count)
        if color == "red" and count > red_max:
            red_max = count
        if color == "green" and count > green_max:
            green_max = count
        if color == "blue" and count > blue_max:
            blue_max = count

    power_sum += red_max * green_max * blue_max

print(f"Second part: {power_sum}")

