import sys
from typing import List

NOT_CORRECT_NUMBERS_ERROR_MESSAGE = 'Во введённых данных обнаружены ошибки или отрицательные числа'
ZERO_SUM_ERROR_MESSAGE = 'Сумма всех долей не может быть равна 0'
NO_SHARES_ERROR_MESSAGE = 'Для работы функции необходимо ввести число долей > 0'

def show_shares_as_persantage(shares: List[float]) -> None:
    """
    Принимает список долей и выводит их в виде процентов.

    :param shares: Список долей в виде чисел (float)
    :return: None
    """
    total: int = sum(shares)
    if total == 0: raise ValueError(ZERO_SUM_ERROR_MESSAGE)
    for share in shares:
        print(f'{share/total:.3f}')

def parse_share(share: str) -> float:
    """
    Преобразует введенную строку с долей в число (float).

    :param share: Строка с долей в виде текста
    :return: преобразованная в число строка
    """
    if share.replace('.','',1).isdigit():
        share = float(share)
        if share >= 0:
            return share
    raise ValueError(NOT_CORRECT_NUMBERS_ERROR_MESSAGE)

def shared_construction():
    data: List[str] = sys.stdin.read().split()
    N: int = int(data[0])
    if N < 0: raise ValueError(NO_SHARES_ERROR_MESSAGE)
    shares: List[float]  = [parse_share(data[i+1]) for i in range(N)]
    show_shares_as_persantage(shares)


if __name__ == "__main__":
    shared_construction()
