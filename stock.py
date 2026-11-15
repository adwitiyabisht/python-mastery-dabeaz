class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected a {self._types[1].__name__}')
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected a {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.price * self.shares

    def sell(self, nshares):
        self.shares -= nshares

def read_portfolio(filename):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock.from_row(row)
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('---------- ---------- ----------')
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    import tableformat

    portfolio = read_portfolio('Data/portfolio.csv')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])