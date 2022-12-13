
def weights(weight):
    weight.sort()
    print(weight)
    trips = []
    w = 0
    while w == 0:
        if len(weight) == 1:
            trips.append(weight[w])
            weight.pop(w)
            w = -1
            print(f'w0: {w}')
            break
        if weight[w] > 1.99:
            trips.append(weight[w])
            weight.pop(w)
            print(f'w1: {w}')
        if weight[w] <= 1.99:
            t = len(weight) - 1
            print(f't1: {t}')
            while t > w:
                if weight[w] + weight[t] <= 3.00:
                    trips.append(f'{weight[w]} + {weight[t]}')
                    weight.pop(t)
                    weight.pop(w)
                    print(f'w2: {w} t2: {t}')
                    print(f'trip: {trips} weights: {weight}')
                    break
                else:
                    if len(weight) == 2:
                        weight.pop(w)
                t = t - 1

        print(f'w3: {w}')
        print(f'trip: {trips} weights: {weight}')


    return trips




n = 5
weight = [1.01, 1.99, 2.5, 1.5, 1.01, 1.99, 1.01, 1.1]
print(weights(weight))