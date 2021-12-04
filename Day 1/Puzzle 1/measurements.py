with open('input.txt') as f:
    lines = list(map(int, f.readlines()))

prev = lines[0]
count = 0

for x in lines:
    if x > prev:
        count+=1
    prev=x

print(count)