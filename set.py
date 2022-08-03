t = {'IBM', 'MSFT', 'AA'}
s = set(['IBM', 'MSFT', 'HPE', 'IBM', 'CAT'])

portfolio = [
    ['MA', '20', '34.4'],
    ['BA', '30', '50.5']
]
# Set comprehension
names = {s[0] for s in portfolio}
print(names)

# set operations
a = t | s
print(a)
b = t & s
print(b)
c = t - s
print(c)
d = s - t
print(d)
e = t ^ s
print(e)
t.add('DIS')
print(t)
s.update({'JJ', 'GE', 'ACME'})
print(s)
t.remove('IBM')
print(t)
s.discard('SCOX')
print(s)
