
def bbr(T):
    """ Retourne la liste des indices des cases à
    échanger pour obtenir un tableau à trois couleurs
    trié en bleu/blanc/rouge"""
    TT = list(T) # clone de T
    indtab = []
    b, w, r = 0, 0, len(T)-1
    while w <=r:
        if T[w] == "white":
            w+=1
        elif T[w] == "red":
            TT[w], TT[r] = TT[r], TT[w] 
            indtab += [w, r]
            r-=1
        else:
            TT[w], TT[b] = TT[b], TT[w]
            indtab += [w, b]
            b+=1
            w+=1
    return indtab
    
