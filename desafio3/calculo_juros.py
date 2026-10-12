from datetime import datetime, date

TAXA_DIARIA = 0.025  # 2,5% ao dia

valor = float(input("Valor da conta (R$): ").replace(",", "."))
vencimento = datetime.strptime(input("Data de vencimento (dd/mm/aaaa): "), "%d/%m/%Y").date()

hoje = date.today()
dias_atraso = (hoje - vencimento).days

if dias_atraso <= 0:
    print("A conta ainda não venceu. Não há juros.")
else:
    juros = valor * TAXA_DIARIA * dias_atraso
    total = valor + juros
    print(f"Dias em atraso: {dias_atraso}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor total a pagar: R$ {total:.2f}")
