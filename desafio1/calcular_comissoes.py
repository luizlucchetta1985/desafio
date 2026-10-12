import json
import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

CENTAVO = Decimal("0.01")


def calcular_comissao(valor: Decimal) -> Decimal:
    """Regra de comissão para uma venda."""
    if valor < 100:
        return Decimal("0")
    if valor < 500:
        taxa = Decimal("0.01")
    else:
        taxa = Decimal("0.05")
    return (valor * taxa).quantize(CENTAVO, rounding=ROUND_HALF_UP)


def formatar_brl(valor: Decimal) -> str:
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def main(caminho: str = "vendas.json") -> None:
    with open(caminho, encoding="utf-8") as f:
        # parse_float=Decimal evita erros de arredondamento com dinheiro
        dados = json.load(f, parse_float=Decimal)

    total_vendido = defaultdict(Decimal)
    total_comissao = defaultdict(Decimal)

    for venda in dados["vendas"]:
        vendedor = venda["vendedor"]
        valor = Decimal(venda["valor"])
        total_vendido[vendedor] += valor
        total_comissao[vendedor] += calcular_comissao(valor)

    print(f"{'Vendedor':<18}{'Total vendido':>18}{'Comissão':>14}")
    print("-" * 50)
    for vendedor in total_vendido:
        print(
            f"{vendedor:<18}"
            f"{formatar_brl(total_vendido[vendedor]):>18}"
            f"{formatar_brl(total_comissao[vendedor]):>14}"
        )


if __name__ == "__main__":
    main(*sys.argv[1:2])
