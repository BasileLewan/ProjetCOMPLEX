import random
from Ex2 import gen_carmichael, first_test

CARMICHAEL = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361,
              101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001,
              410041, 449065, 488881, 512461, 530881, 552721, 656601, 658801, 670033, 748657, 825265, 838201, 852841,
              997633, 1024651, 1033669, 1050985, 1082809, 1152271, 1193221, 1461241, 1569457, 1615681, 1773289, 1857241,
              1909001, 2100901, 2113921, 2433601, 2455921, 2508013, 2531845, 2628073, 2704801, 3057601, 3146221,
              3224065, 3581761, 3664585, 3828001, 4335241, 4463641, 4767841, 4903921, 4909177, 5031181, 5049001,
              5148001, 5310721, 5444489, 5481451, 5632705, 5968873, 6049681, 6054985, 6189121, 6313681, 6733693,
              6840001, 6868261, 7207201, 7519441, 7995169, 8134561, 8341201, 8355841, 8719309, 8719921, 8830801,
              8927101, 9439201]

N = 100000  # taille des échantillons de test


def gen_rsa(t):
    """génère 2 nombre positifs au test de Miller-Rabin sur l'intervalle [2^t-1; 2^t["""
    res = []
    for n in range(2 ** (t - 1), 2 ** t):
        if test_miller_rabin(n):
            res.append(n)
            if len(res) == 2:
                break
    if len(res) < 2:
        raise ValueError("Intervalle trop court")
    return res[0] * res[1]


def test_miller_rabin(n, k=1):
    """implémentation du test de Miller-Rabin, renvoie True si un nombre est premier et False s'il est composé
    n : un entier naturel à tester
    k : précision du test (nombre de bases testées pour n)
    """
    h, m = 0, n - 1
    while m % 2 == 0:
        h += 1
        m //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        b = pow(a, m, n)
        if b == 1 or b == n - 1:
            continue
        for _ in range(h - 1):
            if b != n-1 and pow(b, 2, n) == 1:
                return False
            if b == n - 1:
                break
            b = pow(b, 2, n)
        if b != n - 1:
            return False
    return True


print(f"{'*' * 20} probabilité d'erreur {'*' * 20}")

# Carmichael :

err = 0
for _ in range(N):
    i = random.randint(0, len(CARMICHAEL) - 1)
    if test_miller_rabin(CARMICHAEL[i]) != first_test(CARMICHAEL[i]):
        err += 1

print(" - nombres Carmichael : ", err / N)

# nombres composés :

err = 0
for _ in range(N):
    n = random.randint(2, 100000)
    while first_test(n):
        n = random.randint(2, 100000)
    if test_miller_rabin(n) != first_test(n):
        err += 1

print(" - nombres composés : ", err / N)

# nombres aléatoires :

err = 0
for _ in range(N):
    n = random.randint(4, 100000)
    if test_miller_rabin(n) != first_test(n):
        err += 1

print(" - nombres aléatoires : ", err / N)
