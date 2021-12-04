with open('input.txt') as f:
    lines = list(map(int, f.readlines()))

prev = lines[0]
count = 0
for x in range(len(lines)-3):
    window = lines[x] + lines[x+1] + lines[x+2]
    next_window = lines[x+1] + lines[x+2] + lines[x+3]
    if window < next_window:
        count+=1
print(count)