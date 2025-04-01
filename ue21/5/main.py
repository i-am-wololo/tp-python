import random

def fusionner(T1: list[int], T2: list[int]) -> (list[int], int):
    result = []
    i = 0
    j = 0
    while i<len(T1) and j<len(T2):
        if T1[i] < T2[j]:
            result.append(T1[i])
            i+=1
        else:
            result.append(T2[j])
            j+=1

    if i < len(T1):
        for l in range(i, len(T1)):
            result.append(T1[l])

    if j < len(T2):
        for m in range(j, len(T2)):
            result.append(T2[m])

    return result, i+j

def tri_partiel(T: list[int], a: int, b: int) -> int:
    comp = 0
    for i in range(a, b):
        x = T[i]
        j = i
        while j >= a and T[i-1] > x:
            comp +=1
            T[j] = T[j-1]
            j-=1
        T[j] = x
    return comp

def fusion_partiel(T: list[int], a: int, b: int) -> (list, int):
    aab = fusionner(T[:a], T[a:b])
    return aab[0]+T[b:], aab[1]

def tri_morceau(T: list[int], m: int):
    '''
    trier le tableau par séquence de sous tableau de m éléments:
        - trie les m premiers éléments
        - trie les m élements suivants
        - fusionner les elems precedents et les nouveaux
        - continuer tant qu'il reste des élements
    len(T) doit être un multiple de m (?)
    '''

L = ["#!", "@!@", "!!^^!", "@#!!^", "!"]
A = "@!#^"

def diff(ch1: str, ch2: str) -> int:
    isdiff = False
    i = 0
    while isdiff == False and i < len(ch1) and i < len(ch2):
        if ch1[i] != ch2[i]:
            isdiff = True
        i+=1
    return i-1
    

def tri_alien(T: list[str], A: str):
    ''' 
    T: tableau de mots a trier
    A: chaine de caractères representant l'alphabet
    '''
    

