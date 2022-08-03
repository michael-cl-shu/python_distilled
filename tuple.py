# Read file format NAME,SHARES,PRICE

filename = 'portfolio.csv'

portfolio = []
with open(filename) as file:
    for line in file:
        row = line.split(',')
        name = row[0]
        shares = row[1]
        price = row[2]
        holding = (name, shares, price)
        portfolio.append(holding)

print(portfolio[0])
print(portfolio[1])

total = sum([int(shares) * float(price) for _, shares, price in portfolio])
print(f'Total: {total: 0.2f}')
