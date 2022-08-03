def divid(a, b):
    '''
    Returns the remainder of the a dividing by b
    '''
    q = a // b
    r = a - q * b
    return (q, r)


print(divid(31, 7))


def connect(hostname, port, timeout=500):
    pass


connect('localhost', 3000, 300)
connect('localhost', 3000, timeout=3000)
connect(port=3000, hostname='localhost')
