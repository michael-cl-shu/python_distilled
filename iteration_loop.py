ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def num_suf(number):
    if number == 1:
        return 'st'
    elif number == 2:
        return 'nd'
    elif number == 3:
        return 'rd'
    else:
        return 'th'


for n in ll:
    print(f'2 to the {n}{num_suf(n)} power is { 2 ** n }')

for n in range(1, 10):
    print(f'2 to the {n}{num_suf(n)} power is { 2 ** n }')


def print_range(rang):
    for n in rang:
        print(n)


print_range(range(5))
