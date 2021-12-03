import networkx as nx
import matplotlib.pyplot as plt

#Le choix d’un itinéraire
G=nx.DiGraph()
G.add_nodes_from(['N','PM', 'PL', 'G', 'M','L', 'B'])
G.add_weighted_edges_from([('B','N',4),('B','M',9),('B','L',12),('N','PM',2),('N','L',7),('M','L',2.5),('M','G',4.5),('PM','PL',1),('PL','G',4.5),('L','G',1.25)])
nx.draw(G, pos=nx.spring_layout(G), with_labels =True)
plt.show()
plt.savefig("itineraire.jpg")
plt.close()
sol = nx.shortest_path(G, source='B', target='G',weight='weight')
print('Le plus court chemin est :', sol)

#La détermination d’une session d’examen la plus courte possible
G=nx.Graph()
G.add_nodes_from(['C','Elec', 'Info', 'Math', 'Phy'])
G.add_edges_from([('C','Math'),('C','Phy'),('Elec','Info'),('Info','Math'),('Info','Phy'),('Math','Phy')])
nx.draw(G, with_labels =True)
plt.show()
plt.savefig("sessionExam.jpg")
plt.close()
sol = nx.greedy_color(G)
print("Nombre de demi-journées : ", max(sol.values())+1)

#l'exploitation de gisement pétrolier
G=nx.Graph()
G.add_nodes_from(['A','B','C','D','E','F','G','H','I','J'])
G.add_weighted_edges_from([('A','B',2.8),('A','I',3.4),('B','C',3.1),('B','D',2.7),('C','D',2.4),('C','E',2.6),('C','F',3.2),('D','E',2.3),('D','I',2.1),('E','F',3.4), ('E','H',2.5),('F','G',2.9),('G','H',3.6), ('H','I',3.9),('H','J',6.0),('I','J',5.8)])
nx.draw(G, with_labels =True)
plt.show()
plt.savefig("canalisation.jpg")
plt.close()
sol = nx.minimum_spanning_tree(G)
print("Arbre couvrant : ", sol.edges)
val = 0
for e in sol.edges:
    val += G[e[0]][e[1]]['weight']
print('Valeur optimale : ', val)

#La composition d’équipes
G=nx.Graph()
G.add_nodes_from(range(1,9))
G.add_edges_from([(1,2), (1,4), (1,8), (2,3), (2,4), (2,5),(2,6), (4,5),(4,7),(4,8),(5,6),(5,7)])
nx.draw(G, with_labels =True)
plt.show()
plt.savefig("pilotes.jpg")
#plt.close()
sol = nx.maximal_matching(G)
print(sol)
