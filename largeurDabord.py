from collections import deque
def exploreLargeur(graphe, sommet, etat, F, A):
    etat[sommet] = 'exploré'
    F.append(sommet)
    while len(F) > 0:
        v = F.popleft()
        for j in G[v]:
            if etat[j]=='inexploré':
                etat[j] = 'exploré'
                A.append((v,j))
                F.append(j)
#G est représenté par une listes de listes de successeurs
etat = ['inexploré' for _ in range(n)]
F = deque([])
A = []
for i in range(n):
    if etat[i] == 'inexploré':
        exploreLargeur(G, i, etat, F, A)