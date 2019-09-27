import math

# 1(a)
numbers = []

# 1(b)
sumup = 0

# 3
animals = {'cat': 0, 'dog': 0, 'zebra': 0, 'monkey': 0}

rf = 'assn1_input.txt'
af = 'animals.out'
ff = 'fixed.out'

with open(rf) as input_file, open(ff, 'w+') as fixed_file, open(af, 'w+') as animals_file:
    data = input_file.readlines()

    for line in data:

        # 2
        line = line.replace('zerba', 'zebra')
        fixed_file.write(line)

        line = line.strip().split(';')

        # 1
        if len(line) == 1 and line[0].isnumeric():
            numbers.append(int(line[0]))
            sumup += int(line[0])

        # 3
        else:
            for word in line:
                if animals.get(word) != None:
                    animals[word] += 1

    # 1
    sumup = math.sqrt(sumup)
    numbers.sort()
    numbers.reverse()
    animals_file.write(str(numbers) + '\n')
    animals_file.write('%2.2e' % sumup + '\n')

    # 3
    animals_file.write(str(animals) + '\n')
