from datetime import datetime, timedelta

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    ano_atual = hoje.year
    mes_atual = hoje.month
    dia_atual = hoje.day

    ano_nascimento = data_nascimento.year
    mes_nascimento = data_nascimento.month
    dia_nascimento = data_nascimento.day

    idade = ano_atual - ano_nascimento

    # Ajusta a idade se o aniversário ainda não tiver ocorrido este ano
    if (mes_atual < mes_nascimento) or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade -= 1

    return idade

# Função principal
def main():
    # Solicita a data de nascimento ao usuário
    data_nascimento_str = input("Digite sua data de nascimento (no formato YYYY-MM-DD): ")
    try:
        # Converte a string para um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d")
        idade = calcular_idade(data_nascimento)
        print(f"Sua idade é {idade} anos.")
    except ValueError:
        print("Formato de data inválido. Por favor, use o formato YYYY-MM-DD.")

if __name__ == "__main__":
    main()

