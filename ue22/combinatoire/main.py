def factorielle(n):
    if n == 1:
        return 1
    return n*factorielle(n-1)

def binomial(n, p):
    # calcule le coeff binomial
    return (factorielle(n))/(factorielle(n-p)*factorielle(p))

def TrianglePascal(n):
    triangle = [0 for i in range(n+1)]
    ligne = 1
    li = 
    print(triangle)
    while li < n:
