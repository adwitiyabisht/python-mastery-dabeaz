from abc import ABC, abstractmethod

class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(h for h in headers))

    def row(self, rowdata):
        print(','.join(str(r) for r in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> <th>', end='')
        print('</th> <th>'.join(h for h in headers), end='')
        print('</th> </tr>')

    def row(self, rowdata):
        print('<tr> <td>', end='')
        print('</td> <td>'.join(str(r) for r in rowdata), end='')
        print('</td> </tr>')

def create_formatter(fmt):
    if fmt == 'text':
        return HTMLTableFormatter()

    elif fmt == 'csv':
        return CSVTableFormatter()

    elif fmt == 'html':
        return HTMLTableFormatter()

    else:
        raise TypeError("Invalid format")

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a table formatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)