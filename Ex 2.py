import math as ma
import multiprocessing as mp
import time


def first_test(n):
    """ test naïf de primalité
    retourne True si l'entier est premier, et inversement
    n : un entier naturel
    """
    for a in range(2, int(ma.sqrt(n))):
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


def gen_carmicheal(t):
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
                valid = False
                break
        else:
            valid = True
    if valid:
        print(x)


def gen_carmicheal_mp(t):
    """retourne tous les nombres de Carmichael inférieurs à t
    version multiprocess
    t : un réel
    """
    pool = mp.Pool(processes=mp.cpu_count())
    pool.map(worker_proc, range(3, int(t), 2))


def gen_carmicheal_3(t):
    """ genère un nombre de Carmicheal inférieur t à partir de trois diviseurs premiers"""
    t = int(t)
    prime = []
    for n in range(3, t, 2):
        if first_test(n):
            prime.append(n)

    for i_a, a in enumerate(prime):
        for i_b, b in enumerate(prime[:i_a + 1]):
            for c in prime[:i_b + 1]:
                # on  a obtenu 3 premiers, on test si leur produit est Carmichael
                worker_proc(a * b * c)


def gen_carmicheal_3_mp(t):
    """ genère un nombre de Carmicheal inférieur t à partir de trois diviseurs premiers"""
    t = int(t)
    prime = []
    for n in range(3, t, 2):
        if first_test(n):
            prime.append(n)
    test = []
    for i_a, a in enumerate(prime):
        for i_b, b in enumerate(prime[:i_a + 1]):
            ab = a * b
            for c in prime[:i_b + 1]:
                # on  a obtenu 3 premiers, on test si leur produit est Carmichael
                test.append(ab * c)

    pool = mp.Pool(processes=mp.cpu_count())
    pool.map(worker_proc, test)

# pi(1e5) = 9680
# gen_carmicheal(1e5) = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745,
# 63973, 75361]


if __name__ == '__main__':
    t = time.time()
    # _ = gen_carmicheal(1e4)
    print("std : ", str(time.time() - t))
    t = time.time()
    gen_carmicheal_3_mp(500)
    print("mt : ", str(time.time() - t))
