from Ex2 import gen_carmichael, first_test
import random as rd

N = 100000  # taille des échantillons de test


def test_fermat(n, a=0):
    if not a:
        a = rd.randint(2, 100)

    if pow(a, n - 1, n) != 1:
        return False
    return True


print(f"{'*' * 20} probabilité d'erreur {'*' * 20}")

# Carmichael :

# tst = gen_carmicheal(1e5)
tst = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361]
err = 0

for n in tst:
    if test_fermat(n) != first_test(n):
        err += 1

print(" - nombres Carmichael : ", err / len(tst))

# nombres composés :

err = 0
for _ in range(N):
    a, b = rd.randint(2, 100), rd.randint(2, 100)
    if test_fermat(a * b) != first_test(a * b):
        err += 1

print(" - nombres composés : ", err / N)

# nombres aléatoires :

err = 0
for _ in range(N):
    n = rd.randint(2, 10000)
    if test_fermat(n) != first_test(n):
        err += 1

print(" - nombres aléatoires : ", err / N)
