from datetime import datetime


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    """
    transactions_ = []
    for i in transactions:
        if i.get("state") == state:
            transactions_.append(i)
    return transactions_
