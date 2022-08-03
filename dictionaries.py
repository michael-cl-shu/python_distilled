s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 491.10
}

name = s['name']
cost = s['shares'] * s['price']
print(s)
print(f'Name: {name} Cost: {cost: 0.2f}')

s['shares'] = 75
s['date'] = '2007-06-06'
print(s)

prices = {
    'GOOG': 290.1,
    'APPL': 123.5,
    'IBM': 91.5,
    'MSFT': 80.5
}
print(prices)
if 'IBM' in prices:
    p = prices['IBM']
else:
    p = 0.0
print(p)
# short hand for the if else logic above
r = prices.get('OLHO', 0.0)
print(r)

# delete a key value pair
del prices['GOOG']
print(prices)

prices[('ABBA', '2020-01-01')] = 345.7

print(prices)

portfolio = [
    ('ACME', 50, 92.34),
    ('IBM', 75, 102.25),
    ('PHP', 40, 74.50),
    ('IBM', 50, 124.75)
]

print(portfolio)
total_shares = {s[0]: 0 for s in portfolio}
print(total_shares)

for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares)

pairs = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
print(pairs)
d = dict(pairs)
print(d)
# To get dictionary keys
syms = list(d)
print(syms)
pk = d.keys()
print(pk)
# To get values
values = d.values()
print(values)
# To get items
for sym, price in pairs:
    print(f'{sym}: {price}')
