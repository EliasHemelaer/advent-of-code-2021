with open('input.txt') as f:
    lines = f.readlines()

num = 0
gamma = ""
epsilon = ""

for i in range(len(lines[0])-1):
    for line in lines:
        if int(line[i]) == 0:
            num -= 1
        elif int(line[i]) == 1:
            num += 1
    print(f'Nummer {i}: {num}')
    if num < 0:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
    num = 0

print(int(gamma, 2) * int(epsilon, 2))