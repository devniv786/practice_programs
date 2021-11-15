import itertools

if __name__=="__main__":
    prices = [1, 2, 5, 7, 3, 8, 2, 7]
    com = list(itertools.combinations(prices,2))
    d = {}
    for c in com:
        d[c] = abs(c[0]-c[1])
    print(d)

    max_profit = max(d.values())
    for k,v in d.items():
        if v == max_profit:
            print(k)


