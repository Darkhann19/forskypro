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


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
       Сортирует список транзакций по дате.

       """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )