FILE = 'day1/input.txt'

with open(FILE, encoding='utf8') as file:
    lines = file.readlines()

calibration_values = []
for line in lines:
    numbers = [c for c in line if c.isdigit()]
    calibration_values.append(int(numbers[0] + numbers[-1]))

print(f"Result: {sum(calibration_values)}")
