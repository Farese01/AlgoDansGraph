# Réitération de la fonction creeListeSucc de l'exercice 1 du tp 1, renvoie une liste de listes de successeurs de chaque sommet du graphe
def creeListeSucc(ordre,listeArcs):
    
    # On crée une liste de listes de la taille de l'ordre du graphe
    liste = []
    for i in range(ordre):
        liste.append([])
    
    # On remplit ces listes avec la destination de chaque sommet
    for arc in listeArcs:
        liste[arc[0]].append(arc[1])

    return liste

def add_weight_to_edge_list(graphe):
    edges = list(graphe.edges())

    output = []

    for edge in edges:
        weight = graphe[edge[0]][edge[1]]["weight"]
        new_tuple = (edge[0],edge[1],weight)
        output.append(new_tuple)

    return output
