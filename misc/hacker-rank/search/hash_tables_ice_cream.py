def whatFlavors(cost, money):
    d_cost = {}
    for idx1, i in enumerate(cost):
        if i in d_cost:
            d_cost[i].append(idx1 + 1)
        else:
            d_cost[i] = [idx1 + 1]
    for idx1, i in enumerate(cost):
        if i > money:
            continue
        d = money - i
        if d in d_cost:
            for idx in d_cost[d]:
                if idx1 + 1 != idx:
                    if idx1 + 1 > idx:
                        print(str(idx) + " " + str(idx1 + 1))
                        return
                    else:
                        print(str(idx1 + 1) + " " + str(idx))
                        return


cost = [2, 1, 3, 5, 6]
money = 5
whatFlavors(cost, money)
