with open('Data/portfolio.dat', 'rt') as f:
    cost = sum(int(line.split()[1]) * float(line.split()[2]) for line in f)

print(cost)