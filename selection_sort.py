from numpy import array

T = array([5, 2, 3, 1])
n = 4

def lecture():
    global k
    valid = False
    while not valid:
        k = int(input("k = "))
        valid = 1 <= k <= 20

def posmin(i, n, T):
    pmin = i
    for j in range(i + 1, n):
        if (T[j] < T[pmin]):
            pmin = j

    return pmin

def tri_selection(n, T):
    for i in range(0, n - 1):
        pm = posmin(i, n, T)
        if i != pm:
            T[i], T[pm] = T[pm], T[i]

def affiche(k, n, T):
    nb, i = 1, 1
    while (i < n) and (nb < k):
        if T[i] > T[i - 1]:
            nb += 1
        i += 1

    if nb == k:
        print("Le", k, "eme plus petit element est", T[i-1])
    else:
        print("Le", k, "eme plus petit element n'existe pas")

lecture()
tri_selection(4, T)
affiche(k, n, T)