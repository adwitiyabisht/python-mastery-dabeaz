def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        cost = 0
        for line in f:
            try:
                fields = line.split()
                cost += int(fields[1]) * float(fields[2])
            except ValueError as e:
                print(f"Couldn't parse: {line}")
                print(f"Reason: {e}")

        return cost

if __name__ == '__main__':
    print(portfolio_cost("Data/portfolio.dat"))