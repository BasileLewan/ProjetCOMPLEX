import math as ma
import multiprocessing as mp
import time
import matplotlib.pyplot as plt
import random as rd


def first_test(n):
    """ test naïf de primalité
    retourne True si l'entier est premier, et inversement
    n : un entier naturel
    """
    for a in range(2, int(ma.sqrt(n) + 1)):
        if n % a == 0:
            return False
    return True


def pi(x):
    """retourne le nombre de premiers inférieurs à x
    X : un réel
    """
    cpt = 0
    for n in range(1, int(x)):
        if first_test(n):
            cpt += 1
    return cpt


def gen_carmichael(t):
    """retourne tous les nombres de Carmichael inférieurs à x
    t : un réel
    """
    res = []
    for x in range(3, int(t), 2):  # les nombres de Carmichael sont impairs
        valid = False
        for y in range(2, x):
            if ma.gcd(x, y) == 1:
                if pow(y, x-1, x) != 1:
                    valid = False
                    break
            else:
                valid = True
        if valid:
            res.append(x)

    return res


def worker_proc(x):
    valid = False
    for y in range(2, x):
        if ma.gcd(x, y) == 1:
            if pow(y, x - 1, x) != 1:
                return
        else:
            valid = True
    if valid:
        print(x)


def gen_carmichael_mp(t):
    """retourne tous les nombres de Carmichael inférieurs à t
    version multiprocess
    t : un réel
    """
    pool = mp.Pool(processes=mp.cpu_count())
    pool.map(worker_proc, range(3, int(t), 2))


def gen_carmichael_3(k):
    """ genère les nombres de Carmicheal de longueru binaire k à partir de trois diviseurs premiers
    k : un entier
    """
    # t = int(t)
    prime = []
    for n in range(3, 2 ** k, 2):
        if first_test(n):
            prime.append(n)
    res = []
    for i_a, a in enumerate(prime):
        for i_b, b in enumerate(prime[:i_a]):
            ab = a * b
            for c in prime[:i_b]:
                # on  a obtenu 3 premiers, on teste si leur produit est Carmichael
                # worker_proc(a * b * c)
                tst = ab * c - 1
                if ma.ceil(ma.log2(tst)) != k:
                    continue
                if tst % 2 == 0 and tst % (a - 1) == 0 and tst % (b - 1) == 0 and tst % (c - 1) == 0 and a % (b * c) != 0:
                    res.append(tst + 1)
    return sorted(res)


def gen_carmichael_3_all(t):
    """ genère un nombre de Carmicheal inférieur t à partir de trois diviseurs premiers
    version sans contrainte de taille
    """
    t = int(t)
    prime = []
    for n in range(3, t, 2):
        if first_test(n):
            prime.append(n)
    res = []
    for i_a, a in enumerate(prime):
        for i_b, b in enumerate(prime[:i_a]):
            ab = a * b
            for c in prime[:i_b]:
                tst = ab * c - 1
                if tst % 2 == 0 and tst % (a - 1) == 0 and tst % (b - 1) == 0 and tst % (c - 1) == 0 and a % (b * c) != 0:
                    res.append(tst + 1)
    return sorted(res)

# pi(1e5) = 9680
# gen_carmicheal(1e5) = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745,
# 63973, 75361]


def gen_carmichael_2(p):
    """retourne tous les nombre de carmichael de la forme pqr pour un p donné"""
    prime = []
    for n in range(3, 2 * p * (p ** 2 + 1), 2):
        if n == p:
            continue
        if first_test(n):
            prime.append(n)
    res = []
    for i_r, r in enumerate(prime):
        for q in prime[:i_r]:
            tst = p * q * r - 1
            if tst % 2 == 0 and tst % (p - 1) == 0 and tst % (q - 1) == 0 and tst % (r - 1) == 0 and r % (p * q) != 0:
                res.append(tst + 1)
    return sorted(res)


if __name__ == '__main__':
    t = time.time()
    print(len(gen_carmichael(1e4)))
    print("naif : ", str(time.time() - t))
    t = time.time()
    print(len(gen_carmichael_3_all(1e5)))
    print("3 : ", str(time.time() - t))
    t = time.time()
    gen_carmichael_mp(1e5)
    print("mt : ", str(time.time() - t))

