import networkx as nx
import matplotlib.pyplot as plt
import random
from functions import add_weight_to_edge_list
import time

# Création du graphe
graphe = {
    "sommets": [0,1,2,3,4,5,6,7,8,9],
    "arcs": [
        # Format : (source,destination,poids)
        (0,1,2.8),
        (0,8,3.4),
        (1,2,3.1),
        (1,3,2.7),
        (2,3,2.4),
        (2,4,2.6),
        (2,5,3.2),
        (3,4,2.3),
        (3,8,2.1),
        (4,5,3.4),
        (4,7,2.5),
        (5,6,2.9),
        (6,7,3.6),
        (7,8,3.9),
        (7,9,6.0),
        (8,9,5.8)
    ],
    "ordre": 10
}

# ----- Question 1 -----

def kruskal(listeAretes,ordre): 

    listeAretes = sorted(listeAretes, key=lambda arete: arete[2])

    listeArbre = []
    v = 0
    j = 0 
    cpt = 0
    c = [i for i in range(ordre)]
    m=len(listeAretes)

    while (cpt<ordre and j<m):
        k = listeAretes[j][0]
        l = listeAretes[j][1]
        
        if(c[k] != c[l]):
            listeArbre.append(listeAretes[j])
            v += listeAretes[j][2]
            cpt += 1
            
            tmp = c[k]
            for i in range(ordre):
               if  c[i] == tmp:
                   c[i] = c[l]
        j = j + 1   
    return {
        "sommets": c,
        "arcs": listeArbre
    }

# print(kruskal(graphe["arcs"],graphe["ordre"]))

# ----- Question 2 -----

# Arbre couvrant via kruskal()
arbre_couvrant = kruskal(graphe["arcs"],graphe["ordre"])

# arbre couvrant sous la forme d'un graphe networkx
arbre_couvrant_nx = nx.Graph()
arbre_couvrant_nx.add_nodes_from(arbre_couvrant["sommets"])
arbre_couvrant_nx.add_weighted_edges_from(arbre_couvrant["arcs"])

# Visualisation via networkx et pyplot de l'arbre couvrant obtenu via kruskal()
nx.draw(arbre_couvrant_nx, with_labels = True)
# plt.show()

# graphe initial sous la forme d'un graphe networkx
graphe_nx = nx.Graph()
graphe_nx.add_nodes_from(graphe["sommets"])
graphe_nx.add_weighted_edges_from(graphe["arcs"])

# arbre couvrant via la fonction nx.minimum_spanning_tree() sur le graphe original
spanning_tree = nx.minimum_spanning_tree(graphe_nx)

# Visualisation via networkx et pyplot de l'arbre couvrant obtenu via nx.minimum_spanning_tree()
nx.draw(spanning_tree, with_labels=True)
# plt.show()

# ----- Question 3 -----

def graphe_aleatoire(ordre,densite): # Fonction permettant de générer un graphe aléatoire d'ordre et de densité (entre 0 et 1) donnés, non-orienté
    return nx.gnp_random_graph(ordre, densite, seed=None,directed=False)

# Processus :
# 1. On crée un graphe aléatoire
# 2. On ajoute à ce graphe aléatoire un poids aléatoire entre 2 et 50 pour chacune de ces arêtes, grâce à une boucle for (qui itère sur chaque arête du graphe)
# 3. On crée une variable qui contient l'ordre du graphe, et une variable contenant la liste des arêtes valuées, que l'on formate grâce à la fonction add_weight_to_edge_list()

graphe_aleatoire_100 = graphe_aleatoire(100,0.7)
for edge in graphe_aleatoire_100.edges():
    i = edge[0]
    j = edge[1]
    graphe_aleatoire_100[i][j]['weight'] = random.randint(2,50)

graphe_aleatoire_100_ordre = graphe_aleatoire_100.order()
graphe_aleatoire_100_arcs = add_weight_to_edge_list(graphe_aleatoire_100)

graphe_aleatoire_1000 = graphe_aleatoire(1000,0.7)
for edge in graphe_aleatoire_1000.edges():
    i = edge[0]
    j = edge[1]
    graphe_aleatoire_1000[i][j]['weight'] = random.randint(2,50)

graphe_aleatoire_1000_ordre = graphe_aleatoire_1000.order()
graphe_aleatoire_1000_arcs = add_weight_to_edge_list(graphe_aleatoire_1000)

graphe_aleatoire_2000 = graphe_aleatoire(2000,0.7)
for edge in graphe_aleatoire_2000.edges():
    i = edge[0]
    j = edge[1]
    graphe_aleatoire_2000[i][j]['weight'] = random.randint(2,50)

graphe_aleatoire_2000_ordre = graphe_aleatoire_2000.order()
graphe_aleatoire_2000_arcs = add_weight_to_edge_list(graphe_aleatoire_2000)

def kruskal_with_time(listeAretes,ordre):
    start_time = time.time()

    result = kruskal(listeAretes,ordre)

    duration = time.time()-start_time
    print("La durée d'exécution en secondes de kruskal_with_time() est : "+str(duration)+" secondes.")

    return result

kruskal_with_time(graphe_aleatoire_100_arcs,graphe_aleatoire_100_ordre)
kruskal_with_time(graphe_aleatoire_1000_arcs,graphe_aleatoire_1000_ordre)
kruskal_with_time(graphe_aleatoire_2000_arcs,graphe_aleatoire_2000_ordre)

# ----- Question 4 -----

# On peut utiliser la méthode nx.is_connected().
# Si G n'est pas connexe, E*T n'existe pas car il n'existe pas d'arbre couvrant dans un graphe non-connexe.

print("Connexité du graphe aléatoire d'ordre 100 : "+str(nx.is_connected(graphe_aleatoire_100)))
print("Connexité du graphe aléatoire d'ordre 1000 : "+str(nx.is_connected(graphe_aleatoire_1000)))
print("Connexité du graphe aléatoire d'ordre 2000 : "+str(nx.is_connected(graphe_aleatoire_2000)))