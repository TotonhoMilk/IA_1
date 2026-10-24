# ---------------------------------------------------------------------
# Objetivo desta célula: descobrir em que máquina e em que versão do
# Python o nosso código está rodando. É a primeira coisa que se checa
# quando algo dá errado ("funciona na minha máquina" costuma ser um
# problema de versão diferente).
# Importamos as duas bibliotecas centrais da disciplina e conferimos
# suas versões. Se alguma linha der erro, é sinal de que a biblioteca
# não está instalada — e aí o comando comentado abaixo resolve.
#
# !pip install pandas numpy      <- descomente esta linha só se der erro
# ---------------------------------------------------------------------

import platform  # módulo com informações sobre o sistema operacional
import sys  # módulo com informações sobre o interpretador Python

import numpy as np  # "as np" cria um APELIDO: escreveremos np em vez de numpy
import pandas as pd  # idem para pandas -> pd

# sys.version é um texto longo, algo como "3.11.8 (main, Feb 2024) [GCC 11]".
# O método .split() quebra esse texto em pedaços separados por espaço e
# devolve uma lista; [0] pega o primeiro pedaço, que é só o número da versão.
versao_python = sys.version.split()[0]

# platform.system() devolve o nome do sistema ("Linux", "Windows", "Darwin").
# platform.release() devolve a versão do sistema.
sistema = platform.system()
versao_sistema = platform.release()

# A função print() exibe valores na tela. Quando passamos vários valores
# separados por vírgula, o Python os imprime lado a lado, separados por espaço.
print("Versão do Python:", versao_python)
print("Sistema:", sistema, versao_sistema)
print()

# Todo módulo bem construído guarda a própria versão no atributo __version__.
# Os dois underscores de cada lado indicam um atributo "especial" do Python.
print("numpy :", np.__version__)
print("pandas:", pd.__version__)
print()


# ---------------------------------------------------------------------
# Esta célula contém o Dicionário de coordenadas da Asa Sul, em formato
# UTM(H) por apresentar os valores reais em metros, podendo ser usado
# diretamente em um array no Numpy, calculando distâncias com aritmética
# básica
# ---------------------------------------------------------------------

# Dicionário que consta como chave as quadras da Asa sul do Plano Piloto de
# Brasília-DF, e como valores as coordenadas aproximadas UTM(H) para os pontos
# de polso e desembarque dos drones - Dronepontos.
MAPA_COORDENADA = {
    "central": "23S 189581 8248262",
    "sqs_302": "23S 190135 8250803",
    "sqs_102": "23S 190436 8250690",
    "sqs_202": "23S 190696 8250401",
    "sqs_402": "23S 191073 8250270",
    "sqs_303": "23S 189957 8250570",
    "sqs_103": "23S 190197 8250476",
    "sqs_203": "23S 190510 8250138",
    "sqs_403": "23S 190867 8249959",
    "sqs_304": "23S 189650 8250336",
    "sqs_104": "23S 190018 8250101",
    "sqs_204": "23S 190293 8249900",
    "sqs_404": "23S 190521 8249662",
    "sqs_305": "23S 189482 8250094",
    "sqs_105": "23S 189678 8249800",
    "sqs_205": "23S 190045 8249543",
    "sqs_405": "23S 190244 8249419",
    "sqs_306": "23S 189329 8249816",
    "sqs_106": "23S 189517 8249596",
    "sqs_206": "23S 189717 8249312",
    "sqs_406": "23S 190065 8249117",
    "sqs_307": "23S 189014 8249644",
    "sqs_107": "23S 189232 8249415",
    "sqs_207": "23S 189502 8249033",
    "sqs_407": "23S 189754 8248847",
    "sqs_308": "23S 188813 8249429",
    "sqs_108": "23S 188905 8249230",
    "sqs_208": "23S 189242 8248813",
    "sqs_408": "23S 189298 8248589",
    "sqs_309": "23S 188398 8249191",
    "sqs_109": "23S 188682 8248971",
    "sqs_209": "23S 188928 8248583",
    "sqs_409": "23S 188950 8248343",
    "sqs_310": "23S 188252 8248953",
    "sqs_110": "23S 188409 8248715",
    "sqs_210": "23S 188725 8248384",
    "sqs_410": "23S 188949 8248170",
    "sqs_311": "23S 187886 8248875",
    "sqs_111": "23S 188075 8248512",
    "sqs_211": "23S 188346 8248191",
    "sqs_411": "23S 188497 8247974",
    "sqs_312": "23S 187526 8248555",
    "sqs_112": "23S 187765 8248243",
    "sqs_212": "23S 188017 8247862",
    "sqs_412": "23S 188193 8247693",
    "sqs_313": "23S 187216 8248380",
    "sqs_113": "23S 187517 8248051",
    "sqs_213": "23S 187734 8247734",
    "sqs_413": "23S 188004 8247422",
    "sqs_314": "23S 186990 8248071",
    "sqs_114": "23S 187229 8248012",
    "sqs_214": "23S 187530 8247506",
    "sqs_414": "23S 187651 8247291",
    "sqs_315": "23S 186749 8247880",
    "sqs_115": "23S 186966 8247683",
    "sqs_215": "23S 187187 8247304",
    "sqs_415": "23S 187313 8247049",
    "sqs_316": "23S 186412 8247748",
    "sqs_116": "23S 186599 8247435",
    "sqs_216": "23S 186873 8247112",
    "sqs_416": "23S 187138 8246884",
}

# Cria duas variáveis com os valores das coordenadas (X, Y) da quadra
# SQS 410 para exemplo.
sqs_410_X = MAPA_COORDENADA["sqs_410"].split()[1]
sqs_410_Y = MAPA_COORDENADA["sqs_410"].split()[2]

# Ilustra a quantidade de Dronepontos a partir do Dicionário de coordenadas
print(f"Quantidade de Dronepontos: {len(MAPA_COORDENADA)}")
print()

# Expõe o exemplo de coordenadas X, Y para a quadra SQS 410.
print("Exemplo de coordenada da quadra SQS 410:")
print(f"Este  (Eixo X): {sqs_410_X}  metros")
print(f"Norte (Eixo Y): {sqs_410_Y} metros")
print()


# ---------------------------------------------------------------------
# Esta célula cria um dicionário com os nomes das quadras como valores
# chaves e uma tupla com as coordenadas como valor.
# ---------------------------------------------------------------------

COORD = {}
for drone in MAPA_COORDENADA:
    x = int(MAPA_COORDENADA[drone].split()[1])
    y = int(MAPA_COORDENADA[drone].split()[2])
    COORD[drone] = (x, y)

print("+------------------------------+")
print("|         DRONEPONTOS          |")
print("+------------------------------+")
print("|                              |")
print(f"| {list(COORD)[0]} -> {COORD['central']} |")
print("|                              |")

cont = 0
for droneporto, coordenada in COORD.items():
    if droneporto == "central":
        continue
    if cont == 3:
        print(f"| {droneporto} -> {coordenada} |")
        print("|                              |")
        cont = 0
    else:
        print(f"| {droneporto} -> {coordenada} |")
        cont += 1

print("+------------------------------+")
print()


# ---------------------------------------------------------------------
# Célula que cria o grafo.
# ---------------------------------------------------------------------
import math
import matplotlib.pyplot as plt
import networkx as nx

# 1. Tratar coordenadas (X, Y)
coords = {}
for nome, texto in MAPA_COORDENADA.items():
    _, x, y = texto.split()
    coords[nome] = (float(x), float(y))


# Função de distância física em metros
def obter_distancia(u, v):
    x1, y1 = coords[u]
    x2, y2 = coords[v]
    return math.hypot(x2 - x1, y2 - y1)


# 2. Inicializar Grafo
G = nx.Graph()
for nome, pos in coords.items():
    G.add_node(nome, pos=pos)

# 3. Regras estritas de Vizinhança Ortogonal (Sem Diagonais)
quadras = [n for n in coords.keys() if n != "central"]

for q in quadras:
    prefixo, num_str = q.split("_")
    faixa = int(num_str[0])  # Ex: 3, 1, 2 ou 4
    numero = int(num_str[1:])  # Ex: 02, 03... 16

    # A) Conexão Horizontal: Quadra seguinte na mesma faixa (ex: 102 <-> 103)
    vizinho_horiz = f"sqs_{faixa}{numero + 1:02d}"
    if vizinho_horiz in coords:
        dist = obter_distancia(q, vizinho_horiz)
        G.add_edge(q, vizinho_horiz, weight=dist)

    # B) Conexão Vertical: Faixas vizinhas da mesma quadra (300 <-> 100 <-> 200 <-> 400)
    mapeamento_vertical = {3: [1], 1: [3, 2], 2: [1, 4], 4: [2]}
    for faixa_vizinha in mapeamento_vertical[faixa]:
        vizinho_vert = f"sqs_{faixa_vizinha}{numero:02d}"
        if vizinho_vert in coords:
            dist = obter_distancia(q, vizinho_vert)
            G.add_edge(q, vizinho_vert, weight=dist)

# 4. Conectar a Central à quadra mais próxima da faixa 200/400 (SQS 208 ou SQS 408)
central_vizinhos = ["sqs_408"]
for v in central_vizinhos:
    dist = obter_distancia("central", v)
    G.add_edge("central", v, weight=dist)

# 5. Visualizar
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect("equal")

pos = nx.get_node_attributes(G, "pos")
nos_quadras = [n for n in G.nodes() if n != "central"]

nx.draw_networkx_nodes(G, pos, nodelist=nos_quadras, node_color="black", node_size=20)
nx.draw_networkx_nodes(
    G, pos, nodelist=["central"], node_color="red", node_size=160, label="Central"
)
nx.draw_networkx_edges(G, pos, edge_color="red", alpha=0.6, width=1.2)

plt.title(
    "Malha Ortogonal de Entregas - Asa Sul (Distâncias Reais em Metros)",
    fontsize=12,
)
plt.xlabel("UTM Este (m)")
plt.ylabel("UTM Norte (m)")
plt.grid(True, linestyle="--", alpha=0.3)
plt.show()


# ---------------------------------------------------------------------
# Célula que cria o dicionário de dicionário com pesos.
# ---------------------------------------------------------------------
# 1. Gerar o dicionário no formato solicitado
MAPA = {}

for no in G.nodes():
    MAPA[no] = {}
    for vizinho in G.neighbors(no):
        # Captura o peso (distância em metros) da aresta entre 'no' e 'vizinho'
        distancia = G[no][vizinho]["weight"]
        # Arredonda para 2 casas decimais (opcional)
        MAPA[no][vizinho] = round(distancia, 2)

for n in MAPA.items():
    print(n)

qtd_caminhos = sum(len(v) for v in MAPA.values()) // 2
print("\nEstradas no mapa:", qtd_caminhos)


# ---------------------------------------------------------------------
# AUDITORIA DO MAPA — duas verificações antes de confiar nos dados.
#
# Variável:
#   problemas -> lista que acumula as inconsistências encontradas
# ---------------------------------------------------------------------

problemas = []  # a lista começa vazia: nenhum erro ainda

# .items() percorre o dicionário devolvendo o par (chave, valor) de cada vez.
for cidade, vizinhos in MAPA.items():
    for vizinho, distancia in vizinhos.items():
        # Verificação 1: a cidade vizinha existe como chave no mapa?
        if vizinho not in MAPA:
            problemas.append(f"{vizinho} aparece como vizinha mas não existe")

        # Verificação 2: a distância é a mesma nos dois sentidos?
        # .get() consulta com segurança: devolve None se a chave não existir,
        # em vez de interromper o programa com KeyError.
        elif MAPA[vizinho].get(cidade) != distancia:
            problemas.append(f"{cidade}-{vizinho}: assimetria de distância")

if problemas:
    print("Problemas encontrados:")
    for p in problemas:
        print("  -", p)
else:
    print(
        f"Mapa íntegro: {len(MAPA_COORDENADA)} dronepontos, {qtd_caminhos} estradas, todas simétricas."
    )
print()


# ---------------------------------------------------------------------
# As três consultas que todo algoritmo de busca faz ao mapa.
# ---------------------------------------------------------------------

cidade_atual = "sqs_106"

# PERGUNTA 1 — "para onde eu posso ir a partir daqui?"
# list() converte as chaves em lista, só para imprimir de forma legível.
print("Vizinhos de", cidade_atual, "->", list(MAPA[cidade_atual].keys()))

# PERGUNTA 2 — "quanto custa cada uma dessas estradas?"
print("Custos              ->", MAPA[cidade_atual])

# PERGUNTA 3 — "quanto custa ir daqui para uma cidade específica?"
print("SQS 106   ->   SQS 206:", MAPA["sqs_106"]["sqs_206"], "metros")

print()  # print() sem argumentos apenas pula uma linha

# O padrão que vai aparecer DENTRO de todos os algoritmos:
# percorrer os vizinhos e seus custos ao mesmo tempo, com .items().
# A f-string usa :16s para alinhar o nome em 16 caracteres, deixando
# a saída em colunas; :3d faz o mesmo com um número inteiro.
for vizinho, custo in MAPA[cidade_atual].items():
    print(f"  de {cidade_atual} para {vizinho:6s} custa {custo:3.2f} metros")

# =====================================================================
# TODO 1 — Complete a função abaixo.
#
# custo_do_caminho(caminho) recebe uma lista de cidades e devolve a
# soma dos custos de cada trecho percorrido.
#
# Exemplo: ["Arad", "Sibiu"] deve devolver 140.
# =====================================================================


def custo_do_caminho(caminho):
    """Soma os custos de passo ao longo de uma lista de cidades.

    Parâmetro:
        caminho (list): lista de cidades em ordem, ex. ["Arad", "Sibiu"].

    Devolve:
        int: o custo total do caminho, em quilômetros.
    """
    # Apague a linha abaixo e escreva sua solução.
    # return None
    custo = 0
    for i in range(len(caminho) - 1):
        custo += MAPA[caminho[i]][caminho[i + 1]]
    return custo


# =====================================================================
# TODO 1 — Complete a função abaixo.
#
# custo_do_caminho(caminho) recebe uma lista de cidades e devolve a
# soma dos custos de cada trecho percorrido.
#
# Exemplo: ["Arad", "Sibiu"] deve devolver 140.
# =====================================================================


def custo_do_caminho(caminho):
    """Soma os custos de passo ao longo de uma lista de cidades.

    Parâmetro:
        caminho (list): lista de cidades em ordem, ex. ["Arad", "Sibiu"].

    Devolve:
        int: o custo total do caminho, em quilômetros.
    """
    # Apague a linha abaixo e escreva sua solução.
    # return None
    custo = 0
    for i in range(len(caminho) - 1):
        custo += MAPA[caminho[i]][caminho[i + 1]]
    return custo


# ------------------- teste automático, não precisa alterar -------------------
rota_cntl_316_1 = [
    "central",
    "sqs_408",
    "sqs_208",
    "sqs_209",
    "sqs_210",
    "sqs_110",
    "sqs_111",
    "sqs_112",
    "sqs_113",
    "sqs_114",
    "sqs_314",
    "sqs_315",
    "sqs_316",
]

rota_cntl_316_2 = [
    "central",
    "sqs_408",
    "sqs_409",
    "sqs_410",
    "sqs_411",
    "sqs_412",
    "sqs_413",
    "sqs_414",
    "sqs_415",
    "sqs_416",
    "sqs_216",
    "sqs_116",
    "sqs_316",
]

resultado_1 = custo_do_caminho(rota_cntl_316_1)
resultado_2 = custo_do_caminho(rota_cntl_316_2)

print()
if resultado_1 == 4115.63 and resultado_2 == 4439.17:
    print("Tudo Correto!")
    print("   Rota 1 de central a SQS 316:", resultado_1, "metros")
    print("   Rota 2 de central a SQS 316:", resultado_2, "metros")
else:
    print("Resultado incorreto!")
    print("   Rota 1 de central a SQS 316:", resultado_1, "metros")
    print("   Rota 2 de central a SQS 316:", resultado_2, "metros")
