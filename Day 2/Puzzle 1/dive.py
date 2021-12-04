with open('input.txt') as f:
    lines = f.readlines()

hor = 0
depth = 0

for x in lines:
    s = x.split()
    s[1] = int(s[1])
    if s[0] == "forward":
        hor+=s[1]
    elif s[0] == "down":
        depth+=s[1]
    elif s[0] == "up":
        depth-=s[1]

print(hor * depth)