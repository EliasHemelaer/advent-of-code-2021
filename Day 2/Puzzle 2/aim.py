with open('input.txt') as f:
    lines = f.readlines()

hor = 0
depth = 0
aim = 0

for line in lines:
    s = line.split()
    x = int(s[1])
    if s[0] == "forward":
        hor+=x
        depth+=aim*x
    elif s[0] == "down":
        aim+=x
    elif s[0] == "up":
        aim-=x

print(hor * depth)