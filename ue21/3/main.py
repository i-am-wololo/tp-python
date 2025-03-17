import random

def recherche(T, x):
    trouve = False
    i = 0
    while trouve == False or i != len(T):
        if T[i] == x:
            trouve = true
    return trouve

def recherche_instance(n):
    return [random.randint(0, 15) for i in range(n)]

def recherche_meilleur_cas(n, x):
    randlist = [None]
    while randlist[0] != x:
        randlist = recherche_instance(n)
    return randlist

def recherche_pire_cas(n, x):
    randlist = [None]
    while randlist[-1] != x:
        randlist = recherche_instance(n)
    return randlist


# graphe recherche
