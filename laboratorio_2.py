import matplotlib.pyplot as plt

# Mapa - dicionário de dicionário

MAPA = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucareste": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucareste": 101},
    "Bucareste": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucareste": 90},
    "Urziceni": {"Bucareste": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
}

print(f"Quantidade de cidades no mapa: {len(MAPA)}")
print(f"Estradas no mapa: {sum(len(estradas) for estradas in MAPA.values()) // 2}")
print()

# Auditoria do mapa

problemas = []

for cidade, vizinhos in MAPA.items():
    for vizinho, distancia in vizinhos.items():
        if vizinho not in MAPA:
            problemas.append(f"{vizinho} aparece como vizinha, mas não existe.")
        elif MAPA[vizinho].get(cidade) != distancia:
            problemas.append(f"{cidade}-{vizinho}: assimetria de distância.")

if problemas:
    for problema in problemas:
        print("  -", problema)
else:
    print("Mapa íntegro.")
print()


# Consultas que o algoritmo faz ao mapa

cidade_atual = "Sibiu"

# PERGUNTA 1
print("Vizinhos de", cidade_atual, "->", list(MAPA[cidade_atual].keys()))

# PERGUNTA 2
print("Custos            ->", MAPA[cidade_atual])

# PERGUNTA 3
print("Sibiu -> Fagaras  ->", MAPA[cidade_atual]["Fagaras"], "km")
print()

for vizinho, custo in MAPA[cidade_atual].items():
    print(f"  de {cidade_atual} para {vizinho:16s} custa {custo:3d}km")

print()


# Custo do caminho
def custo_do_caminho(caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += MAPA[caminho[i]][caminho[i + 1]]
    return custo


# teste da função custo_do_caminho():
rota_fagaras = ["Arad", "Sibiu", "Fagaras", "Bucareste"]
rota_pitesti = ["Arad", "Sibiu", "Rimnicu Vilcea", "Pitesti", "Bucareste"]

resultado = custo_do_caminho(rota_fagaras)

if resultado is None:
    print("TODO 1 ainda não foi resolvido.")
elif resultado == 450 and custo_do_caminho(rota_pitesti) == 418:
    # Conferimos os dois casos, para garantir que a função realmente soma
    # e não está devolvendo um número fixo.
    print("TODO 1 correto!")
    print("  Rota por Fagaras:", resultado, "km")
    print("  Rota por Pitesti:", custo_do_caminho(rota_pitesti), "km")
    print()
    print("Duas rotas válidas para o mesmo problema, com custos diferentes.")
    print("A diferença é de", resultado - custo_do_caminho(rota_pitesti), "km.")
else:
    print("Resultado inesperado:", resultado, "- esperado 450 para a rota por Fagaras.")

# Vendo o Mapa
COORD = {
    "Arad": (91, 492),
    "Bucareste": (400, 327),
    "Craiova": (253, 288),
    "Drobeta": (165, 299),
    "Eforie": (562, 293),
    "Fagaras": (305, 449),
    "Giurgiu": (375, 270),
    "Hirsova": (534, 350),
    "Iasi": (473, 506),
    "Lugoj": (165, 379),
    "Mehadia": (168, 339),
    "Neamt": (406, 537),
    "Oradea": (131, 571),
    "Pitesti": (320, 368),
    "Rimnicu Vilcea": (233, 410),
    "Sibiu": (207, 457),
    "Timisoara": (94, 410),
    "Urziceni": (456, 350),
    "Vaslui": (509, 444),
    "Zerind": (108, 531),
}

VERMELHO_IESB = "#C8102E"


def desenhar_mapa(caminho=None, expandidos=None, titulo="Mapa da Romênia"):
    """Desenha o mapa; se receber um caminho, pinta-o em vermelho."""
    caminho = caminho or []  # "or []" evita erro quando vem None
    expandidos = expandidos or []

    fig, ax = plt.subplots(figsize=(13, 8))

    # 1) todas as estradas em cinza claro, ao fundo
    ja_desenhadas = set()
    for cidade, vizinhos in MAPA.items():
        for vizinho in vizinhos:
            # o par ordenado evita desenhar a mesma estrada duas vezes
            par = tuple(sorted([cidade, vizinho]))
            if par in ja_desenhadas:
                continue
            ja_desenhadas.add(par)
            x1, y1 = COORD[cidade]
            x2, y2 = COORD[vizinho]
            ax.plot([x1, x2], [y1, y2], color="#DDE2E7", lw=1.6, zorder=1)

    # 2) por cima, as estradas que fazem parte do caminho-solução.
    # zip(caminho, caminho[1:]) forma os pares consecutivos da lista:
    # ["A","B","C"] vira ("A","B") e ("B","C").
    for a, b in zip(caminho, caminho[1:]):
        x1, y1 = COORD[a]
        x2, y2 = COORD[b]
        ax.plot([x1, x2], [y1, y2], color=VERMELHO_IESB, lw=5, alpha=0.45, zorder=2)
        ax.text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            str(MAPA[a][b]),
            fontsize=10,
            color=VERMELHO_IESB,
            ha="center",
            va="center",
            zorder=5,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=VERMELHO_IESB),
        )

    # 3) as cidades
    for cidade, (x, y) in COORD.items():
        if cidade in expandidos:
            ordem = expandidos.index(cidade) + 1  # posição na expansão
            ax.scatter(x, y, s=330, color=VERMELHO_IESB, zorder=3)
            ax.text(
                x,
                y,
                str(ordem),
                fontsize=10,
                color="white",
                ha="center",
                va="center",
                fontweight="bold",
                zorder=4,
            )
        else:
            ax.scatter(
                x,
                y,
                s=90,
                color="white",
                edgecolors="#1F2933",
                linewidths=1.4,
                zorder=3,
            )
        destaque = cidade in caminho or cidade in expandidos
        ax.text(
            x,
            y + 18,
            cidade,
            fontsize=10 if destaque else 9,
            color="#1F2933" if destaque else "#8A94A0",
            ha="center",
            fontweight="bold" if destaque else "normal",
            zorder=6,
        )

    ax.set_title(titulo, fontsize=15, fontweight="bold", loc="left")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


# caminho_teste = ["Arad", "Sibiu", "Fagaras", "Bucareste"]
desenhar_mapa(titulo="O espaço de estados: 20 cidades, 23 estradas")

# Etapa 2 - O mapeamento de conceitos.
