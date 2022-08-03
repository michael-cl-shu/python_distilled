# Read nput line of the format
# 'NAME,SHARE,PRICE'
# For example:
#
# SYM,123,456.789

import sys
if len(sys.argv) != 2:
    raise SystemExit(f'Usage: {sys.argv[0]} filename')

rows = []
with open(sys.argv[1]) as file:
    for line in file:
        rows.append(line.split(','))

values = [int(row[1]) * float(row[2]) for row in rows]
total = sum(values)

print(f'Total cost: {total: 0.2f}')
