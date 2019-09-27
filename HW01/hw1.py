import math

# 1(a)
numbers = []

# 1(b)
sumup = 0

# 3
animals = {}
targets = ['cat', 'dog', 'zebra', 'monkey']

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
            numbers.append(line[0])
            sumup += int(line[0])

        # 3
        else:
            for word in line:
                for tar in targets:
                    if word != tar:
                        continue
                    if animals.get(word):
                        animals[word] += 1
                    else:
                        animals[word] = 1

    # 1
    sumup = math.sqrt(sumup)
    animals_file.write(str(numbers) + '\n')
    animals_file.write('%2e' % sumup + '\n')

    # 3
    animals_file.write(str(animals) + '\n')
