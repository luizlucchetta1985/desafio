produtos = {
    101: {"descricao": "Caneta Azul", "estoque": 150},
    102: {"descricao": "Caderno Universitário", "estoque": 75},
    103: {"descricao": "Borracha Branca", "estoque": 200},
    104: {"descricao": "Lápis Preto HB", "estoque": 320},
    105: {"descricao": "Marcador de Texto Amarelo", "estoque": 90},
}

proximo_id = 1  # identificador único das movimentações


def ler_int(msg):
    try:
        return int(input(msg).strip())
    except ValueError:
        return -1


while True:
    print("\n--- PRODUTOS ---")
    for cod, p in produtos.items():
        print(f"{cod} - {p['descricao']} (estoque: {p['estoque']})")

    codigo = ler_int("\nCódigo do produto (0 para sair): ")
    if codigo == 0:
        break
    if codigo not in produtos:
        print("Produto não encontrado!")
        continue

    p = produtos[codigo]

    tipo = ler_int("Tipo (1 = Entrada, 2 = Saída): ")
    if tipo not in (1, 2):
        print("Tipo inválido!")
        continue

    qtde = ler_int("Quantidade: ")
    if qtde <= 0:
        print("Quantidade inválida!")
        continue

    if tipo == 2 and qtde > p["estoque"]:
        print(f"Estoque insuficiente! Disponível: {p['estoque']}")
        continue

    descricao = input("Descrição da movimentação: ")

    p["estoque"] += qtde if tipo == 1 else -qtde

    print(f"\nMovimentação #{proximo_id} registrada!")
    print(f"Tipo: {'ENTRADA' if tipo == 1 else 'SAÍDA'} | Descrição: {descricao}")
    print(f"Estoque final de {p['descricao']}: {p['estoque']}")
    proximo_id += 1

print("Programa encerrado.")
