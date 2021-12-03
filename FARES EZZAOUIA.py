#!/usr/bin/env python
# coding: utf-8

# In[44]:


from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
def exploreLargeur(graphe, sommet, etat, F, A,prof):
    etat[sommet] = 'exploré'
    F.append(sommet)
    while len(F) > 0:
        v = F.popleft()
        for j in graphe[v]:
            if etat[j]=='inexploré':
                etat[j] = 'exploré'
                A.append((v,j))
                F.append(j)


# In[66]:


def largeur(G):
    n = G.order()
    etat = ['inexploré' for i in range(n)]
    F = deque([])
    A = []
    prof = [0 for i in range (n)]
    verif = [0 for i in range (n)]
    for i in range(n):
        if etat[i] == 'inexploré':
            exploreLargeur(G, i, etat, F, A,prof)
        for j in list(G.nodes()):
            if((etat[j] == 'exploré') and (verif[j] == 0)):
                prof[j] = i
                verif[j] = 1
    return prof


# In[76]:


def biparti(G):
    prof = largeur(G)
    X1 = []
    X2 = []
    listeArc = list(G.edges())
    for i in list(G.nodes()):
        if prof[i]%2 == 0:
            X1.append(i)
        else:
            X2.append(i)
    b = True
    for i in X1:
        for j in X1:
            for t in listeArc:
                if ((i,j)==t or (j,i)==t):
                    b = False
        
    return b,X1,X2
    


# In[102]:


def representationEncolonne(G):
    b,X1,X2 = biparti(G)
    color_map=[]
    if (b):
        p = nx.bipartite_layout(G, X1, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)
        nx.draw(g, with_labels =True, pos = p)
        plt.show()
    else:
        for node in G:
            if node in X1 :
                color_map.append('blue')
            else: 
                color_map.append('red')
        nx.draw(g, node_color=color_map, with_labels=True)
        plt.show()


# In[103]:


g = nx.read_weighted_edgelist("G1.txt",create_using=nx.DiGraph(), nodetype = int)
g_sommets = list(g.nodes())
print(g_sommets)
g_ordre = g.order()
nx.draw(g, with_labels =True)
plt.show()

representationEncolonne(g)


# In[ ]:




