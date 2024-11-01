def yes_or_no(n):
    n2 = set()
    for i in n:
        if i in n2:
            print('Yes')
        else:
            print('No')
            n2.add(i)

yes_or_no([1, 2, 3, 2, 4, 1, 5])
