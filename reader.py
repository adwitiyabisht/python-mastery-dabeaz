import csv
import stock

def read_csv_as_dicts(filename, coltypes):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            records.append({name:func(val) for name, func, val in zip(headers, coltypes, row)})

    return records

def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
