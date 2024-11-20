import networkx as nx
import matplotlib.pyplot as plt
import os

'''
Usamos como base um trabalho do Roger Medonça,
o Código fonte utilizado no trabalho "Conflito de Interesses (Lei 12.813/2013): Contratos, Parentes e Grafos",
apresentado no 7º Seminário Internacional sobre Análise de Dados na Administração Pública, em 22/10/2021

 Link para o Github: https://github.com/rogersmendonca/grafo-conflito-interesses
 Link para a apresentação do Roger Medonça: https://www.youtube.com/watch?v=1E8XQG6crtg&t=3116s
'''

limpa = lambda: os.system('cls' if os.name == 'nt' else 'clear')
ENTER = lambda: input("Clique Enter para continuar")

#Grafo padrão
a = [
        (0, 1, 4), 
        (0, 2, 2), 
        (1, 2, -3), 
        (2, 3, 2), 
        (3, 1, 1)
    ]

#Grafo denso com pesos mistos
b = [
    (0, 1, 10),
    (0, 2, 5),
    (1, 2, 2),
    (1, 3, 1),
    (2, 1, 3),
    (2, 3, 9),
    (2, 4, 2),
    (3, 4, 4),
    (4, 0, 7),
    (4, 3, 6)
]

#Grafo esparso sem pesos negativos
c = [
    (0, 1, 8),
    (0, 2, 1),
    (1, 3, 5),
    (2, 3, 3),
    (3, 4, 4)
]

#Grafo com ciclos negativos
d = [
    (0, 1, 1), 
    (1, 2, 1), 
    (2, 0, -3),  #Ciclo negativo
    (1, 3, 2),
    (3, 4, 1)
]

def johnson_algorithm(graph):
    """
    Implementação do algoritmo de Johnson para encontrar os menores caminhos entre todos os pares de vértices.
    """
    #Adicionar um nó fictício conectado a todos os outros nós com peso 0
    temp_graph = graph.copy()
    temp_graph.add_node('q')
    for node in temp_graph.nodes:
        if node != 'q':
            temp_graph.add_edge('q', node, weight=0)
    
    #Etapa 1: Aplicar Bellman-Ford para calcular os pesos potenciais
    try:
        potentials = nx.single_source_bellman_ford_path_length(temp_graph, 'q')
    except nx.NetworkXUnbounded:
        raise ValueError("O grafo contém ciclos negativos!")

    #Remover o nó fictício
    temp_graph.remove_node('q')
    
    #Recalcular pesos das arestas usando os potenciais
    for u, v, data in graph.edges(data=True):
        data['weight'] += potentials[u] - potentials[v]
    
    #Etapa 2: Aplicar Dijkstra em cada nó do grafo ajustado
    shortest_paths = {}
    for node in graph.nodes:
        lengths = nx.single_source_dijkstra_path_length(graph, node, weight='weight')
        #Ajustar os pesos para os valores originais
        shortest_paths[node] = {v: d + potentials[v] - potentials[node] for v, d in lengths.items()}
    
    return shortest_paths

def visualize_graph(graph):
    """
    Visualiza o grafo usando a biblioteca NetworkX.
    """
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()

#Exemplo de uso
if __name__ == "__main__":
    while True:
        limpa()
        print('''
            ALGORITMO DE JOHNSON
    a) Grafo com pesos (incluindo negativos)
    b) Grafo denso com pesos mistos
    c) Grafo esparso sem pesos negativos
    d) Grafo com ciclos negativos
    e) Encerrar aplicação''')

        opcao = input("\nEscolha a opção desejada: ")
        match opcao:
            case 'a':
                G = nx.DiGraph()
                G.add_weighted_edges_from(a) 


                try:
                    shortest_paths = johnson_algorithm(G)
                    print("Menores caminhos entre todos os pares de nós:")
                    for source, paths in shortest_paths.items():
                        for target, distance in paths.items():
                            print(f"Menor caminho de {source} para {target}: {distance}")
                except ValueError as e:
                    print(e)
                
                print("Visualizando o grafo original:")
                visualize_graph(G)
                ENTER()

            case 'b':
                G = nx.DiGraph()
                G.add_weighted_edges_from(b) 


                try:
                    shortest_paths = johnson_algorithm(G)
                    print("Menores caminhos entre todos os pares de nós:")
                    for source, paths in shortest_paths.items():
                        for target, distance in paths.items():
                            print(f"Menor caminho de {source} para {target}: {distance}")
                except ValueError as e:
                    print(e)
                
                print("Visualizando o grafo original:")
                visualize_graph(G)
                ENTER()

            case 'c':
                G = nx.DiGraph()
                G.add_weighted_edges_from(c) 


                try:
                    shortest_paths = johnson_algorithm(G)
                    print("Menores caminhos entre todos os pares de nós:")
                    for source, paths in shortest_paths.items():
                        for target, distance in paths.items():
                            print(f"Menor caminho de {source} para {target}: {distance}")
                except ValueError as e:
                    print(e)
                
                print("Visualizando o grafo original:")
                visualize_graph(G)
                ENTER()

            case 'd':
                G = nx.DiGraph()
                G.add_weighted_edges_from(d) 


                try:
                    shortest_paths = johnson_algorithm(G)
                    print("Menores caminhos entre todos os pares de nós:")
                    for source, paths in shortest_paths.items():
                        for target, distance in paths.items():
                            print(f"Menor caminho de {source} para {target}: {distance}")
                except ValueError as e:
                    print(e)
                
                print("Visualizando o grafo original:")
                visualize_graph(G)
                ENTER()

            case 'e':
                break

            case _:
                print("Opção inválida!")
                ENTER()
