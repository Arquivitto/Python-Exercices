"""
Este módulo fornece funções para a troca de moeda, cálculo do valor das notas,
e determinação do valor máximo de nova moeda que pode ser obtido após aplicar
uma taxa de câmbio (spread).

Funções:
- exchange_money: Calcula o valor de moeda estrangeira recebido ao trocar uma certa quantia de dinheiro.
- get_change: Calcula o valor de dinheiro restante após trocar uma parte dele.
- get_value_of_bills: Calcula o valor total de um dado número de notas de uma denominação específica.
- get_number_of_bills: Determina quantas notas de uma denominação específica podem ser obtidas de um valor total.
- get_leftover_of_bills: Calcula o valor restante após determinar quantas notas de uma denominação específica podem ser obtidas.
- exchangeable_value: Calcula o valor máximo na nova moeda que pode ser obtido a partir de um orçamento dado, considerando a taxa de câmbio e o spread.

Exemplo de Uso:
    budget_amount = 127.5
    exchange_rate = 1.2
    spread_percentage = 10
    bill_denomination = 5
    max_value = exchangeable_value(budget_amount, exchange_rate, spread_percentage, bill_denomination)
    print(max_value)
"""

def exchange_money(budget_amount: float, exchange_rate: float) -> float:
    """
    Calcula o valor de moeda estrangeira que você pode receber ao trocar uma certa quantia de dinheiro.

    :param budget_amount: float - Quantia de dinheiro que você está planejando trocar.
    :param exchange_rate: float - Valor unitário da moeda estrangeira.
    :return: float - Valor trocado da moeda estrangeira que você pode receber.
    """
    return budget_amount / exchange_rate

def get_change(budget_amount: float, exchanged_value: float) -> float:
    """
    Calcula o valor de dinheiro restante após trocar uma parte dele.

    :param budget_amount: float - Quantia de dinheiro que você possui.
    :param exchanged_value: float - Quantia de dinheiro que você deseja trocar agora.
    :return: float - Valor restante da sua moeda inicial após a troca.
    """
    return budget_amount - exchanged_value

def get_value_of_bills(bill_denomination: int, total_bills: int) -> int:
    """
    Calcula o valor total de um dado número de notas de uma denominação específica.

    :param bill_denomination: int - O valor de uma nota.
    :param total_bills: int - Número total de notas.
    :return: int - Valor calculado das notas.
    """
    return total_bills * bill_denomination

def get_number_of_bills(total_amount: float, bill_denomination: int) -> int:
    """
    Determina quantas notas de uma denominação específica podem ser obtidas de um valor total.

    :param total_amount: float - O valor total inicial.
    :param bill_denomination: int - O valor de uma única nota.
    :return: int - Número de notas que podem ser obtidas a partir do valor total.
    """
    return int(total_amount // bill_denomination)

def get_leftover_of_bills(total_amount: float, bill_denomination: int) -> float:
    """
    Calcula o valor restante após determinar quantas notas de uma denominação específica podem ser obtidas.

    :param total_amount: float - O valor total inicial.
    :param bill_denomination: int - O valor de uma única nota.
    :return: float - O valor que sobra, dado a denominação da nota atual.
    """
    return total_amount % bill_denomination

def exchangeable_value(budget_amount: float, exchange_rate: float, spread_percentage: int, bill_denomination: int) -> int:
    """
    Calcula o valor máximo na nova moeda que pode ser obtido a partir de um orçamento dado, considerando a taxa de câmbio e o spread.

    :param budget_amount: float - A quantia do seu dinheiro que você está planejando trocar.
    :param exchange_rate: float - O valor unitário da moeda estrangeira.
    :param spread_percentage: int - Percentual que é cobrado como taxa de câmbio.
    :param bill_denomination: int - O valor de uma única nota.
    :return: int - Valor máximo que você pode obter.
    """
    # Converte o percentual de spread para decimal
    spread_decimal = spread_percentage / 100.0
    
    # Calcula a nova taxa de câmbio incluindo o spread
    new_exchange_rate = exchange_rate * (1 + spread_decimal)
    
    # Calcula a quantia de moeda estrangeira que podemos obter
    exchanged_money = budget_amount / new_exchange_rate
    
    # Calcula o número de notas inteiras que podemos obter
    number_of_bills = exchanged_money // bill_denomination
    
    # Calcula o valor máximo que podemos obter
    max_value = int(number_of_bills * bill_denomination)
    
    return max_value
