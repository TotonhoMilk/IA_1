import platform
import random
import sys

import numpy as np
import pandas as pd

print(f"Versão do python: {sys.version.split()[0]}")
print(f"Sistema: {platform.system()} {platform.release()}")

print(f"numpy:  {np.__version__}")
print(f"pandas: {pd.__version__}")

local = "A"
esta_sujo = True
custo = 1.5
passos = 10

print("local     =", local, "| tipo:", type(local))
print("esta_sujo =", esta_sujo, "| tipo:", type(esta_sujo))
print("custo     =", custo, "| tipo:", type(custo))
print("passos    =", passos, "| tipo:", type(passos))

percepcao = ("A", "Sujo")

print("A percepção completa:", percepcao)
print("Quantos elementos:", len(percepcao))
print("Elemento na posição 0:", percepcao[0])
print("Elemento na posição 1:", percepcao[1])

local_atual, estado_atual = percepcao

print("Após o desempacotamento -> local:", local_atual, "| estado:", estado_atual)

acoes = ["Aspirar", "Direita", "Esquerda"]
print(f"Ações iniciais: {acoes}")

acoes.append("NadaFazer")
print(f"Depois do append: {acoes}")

print(f"Primeira ação: {acoes[0]}")
print(f"Última ação  : {acoes[-1]}")
print(f"Total de ações: {len(acoes)}")

print(f"'Aspirar' é uma ação válida?: {'Aspirar' in acoes}")
print(f"'Voar' é uma ação válida?:    {'Voar' in acoes}")

mundo = {"A": "Sujo", "B": "Limpo"}
print(f"Estado do mundo: {mundo}")

print(f"O local A está: {mundo['A']}")
print(f"O local B está: {mundo['B']}")

mundo["A"] = "Limpo"
print(f"Depois de aspirar A: {mundo}")

print(f"Locais existentes: {list(mundo.keys())}")
print(f"Condições existentes: {list(mundo.values())}")

print(f"E o local C? {mundo.get('C')}")


def custo_da_acao(acao):
    if acao == "NadaFazer":
        return 0
    return 1


print(f"Custo de aspirar: {custo_da_acao('Aspirar')}")
print(f"Custo de nada a fazer: {custo_da_acao('NadaFazer')}")
print()

print("Custo das ações: ")
for acao in acoes:
    print(f"{acao:12} -> custo: {custo_da_acao(acao)}")

print()

print("Situação das ações: ")
for lugar, estado in mundo.items():
    print(f"O local {lugar} está {estado}")


print()


def conta_sujos(mundo):
    contador = 0
    for valor in mundo.values():
        if valor == "Sujo":
            contador += 1
    return contador


# ------------------- teste automático, não precisa alterar -------------------
resultado = conta_sujos({"A": "Sujo", "B": "Sujo"})

if resultado is None:
    print("TODO 1 ainda não foi resolvido.")
elif resultado == 2:
    # Conferimos também um segundo caso, para garantir que a função não
    # está simplesmente devolvendo 2 sempre.
    if conta_sujos({"A": "Limpo", "B": "Limpo"}) == 0:
        print("TODO 1 correto! Os dois casos de teste passaram.")
    else:
        print("Quase: o caso com tudo limpo deveria devolver 0.")
else:
    print("Resultado inesperado:", resultado, "- esperado: 2")

print()

registros = pd.DataFrame(
    {
        "passo": [1, 2, 3, 4, 5, 6],
        "local": ["A", "A", "B", "B", "A", "B"],
        "estado": ["Sujo", "Limpo", "Sujo", "Limpo", "Limpo", "Limpo"],
        "acao": ["Aspirar", "Direita", "Aspirar", "Esquerda", "Direita", "NadaFazer"],
        "custo": [1, 1, 1, 1, 1, 0],
    }
)

print(registros.head())
print()

print(f"Formato (linhas, colunas): {registros.shape}")
print()

print("Tipos de cada coluna: ")
print(registros.dtypes)
print()

print("Estatistica descritiva:")
print(registros.describe())
print()

coluna_acao = registros["acao"]
print(f"Tipo do resultado: {type(coluna_acao).__name__}")
print()

subtabela = registros[["acao", "custo"]]
print(f"Tipo de resultado: {type(subtabela).__name__}")
print(subtabela)
print()

mascara = registros["custo"] > 0
print("Mascara: uma resposta por linha: ")
print(mascara)
print()

com_custo = registros[mascara]
print("Mascara com custo")
print(com_custo)
print()

print("Mesma coisa escrito de forma compacta")
print(registros[registros["custo"] > 0])
print()

print("Passos do local A que houve custo")
print(registros[(registros["local"] == "A") & (registros["custo"] > 0)])
print()

custo_por_local = registros.groupby("local")["custo"].sum()
print("Custo total por local:")
print(custo_por_local)
print()

print("Quantos passos o agente deu em cada local: ")
print(registros.groupby("local").size())
print()

print("Quantas vezes cada ação foi executada: ")
print(registros["acao"].value_counts())
print()

print("TODO -> Linhas onde a ação foi 'Aspirar'")
print(registros[registros["acao"] == "Aspirar"])
print()


def agente_reativo(percepcao, memoria=None):
    local, estado = percepcao

    if estado == "Sujo":
        return "Aspirar"

    return "Direita" if local == "A" else "Esquerda"


print("Comportamento do agente em cada posição possível:")
for posicao in [("A", "Sujo"), ("A", "Limpo"), ("B", "Sujo"), ("B", "Limpo")]:
    print(f"Percepção: {posicao!s:18s} -> Ação: {agente_reativo(posicao)}")
print()


def simular(agente, mundo_inicial, local_inicial="A", passos=10, verbose=False):
    mundo = dict(mundo_inicial)

    local = local_inicial
    memoria = {}
    pontos = 0
    historico = []

    for passo in range(1, passos + 1):
        percepcao = (local, mundo[local])

        acao = agente(percepcao, memoria)

        if acao == "Aspirar":
            mundo[local] = "Limpo"
        elif acao == "Direita":
            local = "B"
        elif acao == "Esquerda":
            local = "A"

        limpos = sum(1 for espaco in mundo.values() if espaco == "Limpo")
        pontos += limpos

        historico.append(
            {
                "passo": passo,
                "percepcao": str(percepcao),
                "acao": acao,
                "limpos": limpos,
            }
        )

        if verbose:
            print(
                f"passo {passo:2d} | percepção: {percepcao!s:18s} | "
                f"ação: {acao:10s} | limpos agora: {limpos}"
            )

    return pontos, historico


mundo_sujo = {"A": "Sujo", "B": "Sujo"}

print("Simulação do agente reativo simples:")
pontos, historico = simular(agente_reativo, mundo_sujo, passos=8, verbose=True)

print()
print("Pontuação total: ", pontos)

# Transformando o histórico em dados (Dataframe)

tabela_historio = pd.DataFrame(historico)
print("O historico das ações como tabela: ")
print(tabela_historio)
print()

print("Frequencia de cada ação:")
print(tabela_historio["acao"].value_counts())
print()

random.seed(42)


def agente_aleatorio(percepcao, memoria=None):
    _, estado = percepcao

    if estado == "Sujo":
        return "Aspirar"

    return random.choice(["Direita", "Esquerda", "NadaFazer"])


def agente_com_memoria(percepcao, memoria):
    local, estado = percepcao

    memoria[local] = estado

    if estado == "Sujo":
        memoria[local] = "Limpo"
        return "Aspirar"

    outro = "B" if local == "A" else "A"

    if memoria.get(outro) == "Sujo":
        return "NadaFazer"

    return "Direita" if local == "A" else "Esquerda"


agentes = {
    "reativo simples": agente_reativo,
    "aleatório": agente_aleatorio,
    "com memória": agente_com_memoria,
}

cenarios = {
    "ambos sujos": {"A": "Sujo", "B": "Sujo"},
    "só A sujo": {"A": "Sujo", "B": "Limpo"},
    "ambos limpos": {"A": "Limpo", "B": "Limpo"},
}

random.seed(42)

linhas = []

for nome_agente, agente in agentes.items():
    for nome_cenario, mundo0 in cenarios.items():
        pontos, _ = simular(agente, mundo0, passos=10)

        linhas.append(
            {"agente": nome_agente, "cenario": nome_cenario, "pontuação": pontos}
        )

comparativo = pd.DataFrame(linhas)

print("Comparativo simples dataframe: ")
print(comparativo)
print()

tabela_final = comparativo.pivot(index="agente", columns="cenario", values="pontuação")

print("Pontuação em 10 passos, quanto maior melhor:")
print(tabela_final)
print()


def simular_com_penalidade(agente, mundo_inicial, local_inicial="A", passos=10):
    mundo = dict(mundo_inicial)

    local = local_inicial
    memoria = {}
    pontos = 0

    for _ in range(passos):
        percepcao = (local, mundo[local])

        acao = agente(percepcao, memoria)

        if acao == "Aspirar":
            mundo[local] = "Limpo"
        elif acao == "Direita":
            local = "B"
        elif acao == "Esquerda":
            local = "A"

        pontos += sum(1 for espaco in mundo.values() if espaco == "Limpo")

        if acao in ["Direita", "Esquerda"]:
            pontos -= 1

    return pontos


random.seed(42)
print("Comparação com a nova medida")
print("Os dois locais já começam limpos")
print()

for nome_agente, agente in agentes.items():
    p = simular_com_penalidade(agente, {"A": "Limpo", "B": "Limpo"}, passos=10)
    print(f"{nome_agente!s:18} -> {p} pontos")
