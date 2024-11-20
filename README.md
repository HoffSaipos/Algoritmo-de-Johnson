# Algoritmo de Johnson para Menores Caminhos em Grafos
Trabalho feito para a matéria de Estruturas de Dados Avançadas, buscando estruturar em python, o Algoritmo de Johnson.

Este projeto implementa o **algoritmo de Johnson**, que calcula os menores caminhos entre todos os pares de vértices em um grafo ponderado. O algoritmo é ideal para grafos com pesos negativos, desde que não contenham ciclos negativos. A implementação combina os algoritmos de **Bellman-Ford** e **Dijkstra**, aproveitando as vantagens de ambos para garantir eficiência e robustez.

---

## 🛠️ Descrição do Projeto

O algoritmo de Johnson funciona em três etapas principais:

1. **Adição de um Nó Fictício:**
   - Um nó fictício é adicionado ao grafo, conectado a todos os outros vértices com arestas de peso \( 0 \).
   
2. **Reponderação com Bellman-Ford:**
   - Calcula uma função de potencial \( h(v) \) para reponderar as arestas do grafo, eliminando pesos negativos.
   
3. **Cálculo de Menores Caminhos com Dijkstra:**
   - Após a reponderação, o algoritmo de Dijkstra é executado para cada vértice, calculando os menores caminhos entre todos os pares.

No final, as distâncias calculadas são ajustadas de volta para refletir os pesos originais.

---

## 🚀 Funcionalidades

- Calcula menores caminhos entre todos os pares de vértices em grafos com pesos positivos ou negativos.
- Detecta ciclos negativos no grafo (através do algoritmo de Bellman-Ford).
- Visualiza grafos utilizando a biblioteca `matplotlib`.

---

## 📋 Requisitos

Este projeto requer o **Python 3.8** ou superior e as seguintes bibliotecas:

- **`networkx`**:
  - Para modelar o grafo, executar os algoritmos de grafos e calcular os menores caminhos.
- **`matplotlib`**:
  - Para visualizar o grafo e suas conexões.
- **`numpy`** (opcional):
  - Auxilia no tratamento de dados para visualizações e cálculos adicionais.

---

## 🛠️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuprojeto/johnson-algorithm.git
   cd johnson-algorithm

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
    ```

---

## 🧑‍💻 Como Usar

### 1. Defina o Grafo:
No arquivo principal, configure as arestas e os pesos do grafo:

  ```
    edges = [
      (0, 1, 3),
      (1, 2, -2),
      (2, 3, 2),
      (0, 3, 5)
      ]
  ```

### 2. Execute o Algoritmo:
Rode o script para calcular os menores caminhos:
  ```bash
  python main.py
  ```

### 3. Visualize os Resultados:
Os menores caminhos e o grafo serão exibidos no terminal e em uma janela gráfica.

---

## 📊 Exemplos
### Entrada 1: Grafo com Pesos Negativos
```python
edges = [
    (0, 1, 4),
    (1, 2, -5),
    (2, 3, 2),
    (3, 0, 3)
]
```

### Entrada 2: Grafo com Pesos Positivos
```python
edges = [
    (0, 1, 3),
    (1, 2, 2),
    (2, 3, 1),
    (0, 3, 5)
]
```

---

## 📂 Estrutura do Código
```plaintext
├── main.py          # Arquivo principal com a implementação do algoritmo
├── graph_utils.py   # Funções auxiliares para manipulação e visualização de grafos
├── README.md        # Documentação do projeto
├── requirements.txt # Lista de dependências
```

---

## 🔍 Funcionamento do Algoritmo
O algoritmo de Johnson combina as seguintes técnicas:

1. Bellman-Ford: Repondera as arestas para garantir que os pesos sejam não negativos.
2. Dijkstra: Calcula menores caminhos entre todos os pares usando os pesos reponderados.

---

## 👤 Autor
Desenvolvido por Rafael Hoffmann, em um trabaho em conjunto com a Millene Pires e Bruno Santos


