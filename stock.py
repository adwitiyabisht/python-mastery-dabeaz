class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.price * self.shares

    def sell(self, nshares):
        self.shares -= nshares

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('---------- ---------- ----------')
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    import tableformat

    portfolio = read_portfolio('Data/portfolio.csv')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])