import numpy as np
import random
def aco(d, c, n_ants=5, n_iter=10):
    n, tau, best_r, best_d = len(d), np.ones((len(d), len(d))), None, float('inf')
    for _ in range(n_iter):
        for _ in range(n_ants):
            unv, cur, route, dist = set(range(1, n)), 0, [0], 0
            while unv:
                valid = [x for x in unv if x in unv]
                nxt = min(valid, key=lambda x: d[cur][x])
                route.append(nxt); dist += d[cur][nxt]; unv.remove(nxt); cur = nxt
            dist += d[cur][0]; route.append(0)
            if dist < best_d: best_d, best_r = dist, route
        tau *= 0.9; tau[best_r[:-1], best_r[1:]] += 1.0 / best_d
    return best_r, best_d
