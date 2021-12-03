import networkx as nx
import matplotlib.pyplot as plt
import time
from functions import creeListeSucc,add_weight_to_edge_list

# Création du graphe

graphe = {
    "sommets": [0,1,2,3,4,5,6],
    "liste_arcs": [
        # Format : (source,destination,poids)
        (0,1,6),
        (0,2,2),
        (0,3,1),
        (1,2,-3),
        (1,4,7),
        (2,3,-2),
        (2,4,-4),
        (3,5,2),
        (4,5,3),
        (4,6,3),
        (5,6,1)
    ],
    "ordre": 7
}

# ----- Question 1 -----

# Fonction renvoyant le poids d'un arc entre un sommet i et j (float). Prends une liste d'arcs en entrée, ainsi que les sommets i & j.
def get_weight(arcs,i,j):
    INF = float('inf') # Constante matérialisant l'infini

    output_tuple = None

    for tuple in arcs:
        if(tuple[0] == i and tuple[1] == j):
            output_tuple = tuple

    if(output_tuple is not None):
        return output_tuple[2]
    else:
        return INF


# Fonction pcch() de l'exercice 1. Prends en entrée un graphe matérialisé par son ordre et sa liste d'arcs, ainsi qu'un sommet source et un sommet de destination
def pcch(ordre,listeArcs):

    D = [0 for i in range(ordre)] # = ƛ
    C = [0 for i in range(ordre)] # = p

    successeurs = creeListeSucc(ordre,listeArcs)
    
    for i in range(ordre):
        C[i] = 0
        D[i] = get_weight(listeArcs,0,i)

    for k in range(ordre):
        for i in successeurs[k]:
            if(D[k] + get_weight(listeArcs,k,i) < D[i]):
                D[i] = D[k] + get_weight(listeArcs,k,i)
                C[i] = k

    return D[ordre-1]

print(pcch(graphe["ordre"],graphe["liste_arcs"])) # print() de test

# ----- Question 2 -----

g = nx.read_weighted_edgelist("bigDAG.txt",create_using=nx.DiGraph(), nodetype = int)

g_arcs = add_weight_to_edge_list(g)
g_sommets = list(g.nodes())
g_ordre = g.order()

def pcch_with_time(ordre,listeArcs,sommets):
    start_time = time.time()

    result = pcch(ordre,listeArcs,sommets)

    duration = time.time() - start_time
    print("Le temps d'exécution de pcch_with_time() fut de : "+str(duration)+" secondes.")

    return result

def nx_shortest_path_length_with_time(graphe):
    start_time = time.time()

    result = nx.shortest_path_length(graphe)

    duration = time.time() - start_time
    print("Le temps d'exécution de nx_shortest_path_length_with_time() fut de : "+str(duration)+" secondes.")

    return result

# pcch_with_time(g_ordre,g_arcs,g_sommets) # Le temps d'exécution de pcch_with_time() fut de : 989.5400037765503 secondes.
# nx_shortest_path_length_with_time(graphe) # Le temps d'exécution de nx_shortest_path_length_with_time() fut de : 6.198883056640625e-06 secondes.