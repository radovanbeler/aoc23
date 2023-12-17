import re

FILE = 'day2/input.txt'

with open(FILE, encoding='utf8') as file:
    lines = file.readlines()

def is_possible(color, count):
    match color:
        case "red":
            return count <= 12
        case "green":
            return count <= 13
        case "blue":
            return count <= 14
        
id_sum = 0
for line in lines:
    id = int(re.findall(r"Game (\d+):", line)[0])
    draws = re.findall(r"(\d+ \w+)", line)
    possible = True
    for draw in draws:
        count, color = draw.split()
        if not is_possible(color, int(count)):
            possible = False
            break

    if possible:
        id_sum += id

print(f"First part: {id_sum}")

