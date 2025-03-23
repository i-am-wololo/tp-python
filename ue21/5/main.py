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

def fusion_partiel(T: list[int], a: int, b: int) -> int:
    aab = fusionner(T[:a], T[a:b])[0]
    return aab+T[b:]

