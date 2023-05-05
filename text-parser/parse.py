file_name = "input.txt"

file = open(file_name, "r")

lines = file.readlines()

lines = list(map(lambda l: l.lower().strip(), lines))

text_to_find = "computer science".lower()

for i, line in enumerate(lines):
    if text_to_find in line:
        print("Line no. {}: {}".format(i, line))