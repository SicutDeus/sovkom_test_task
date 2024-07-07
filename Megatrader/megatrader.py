import itertools
import sys
class ObligationPackage:
    def __init__(self,total_days, day, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.purchase_day = int(day)
        self.total_days = total_days
        self.NOMINAL = 1000
        self.BASE_DAY_INCOME = 1
        self.FULL_INCOME_DAY_OFFSET = 30
        self.ue_price = self. quantity * self.price * self.NOMINAL / 100
        self.package_income = (
                self.quantity *
                (self.total_days - self.purchase_day + self.FULL_INCOME_DAY_OFFSET) * self.BASE_DAY_INCOME
        )
        self.full_package_income = int(self.NOMINAL * self.quantity + self.package_income - self.ue_price)

    def __str__(self):
        return f"{self.purchase_day} {self.name} {self.price} {self.quantity}"


def parse_input():
    """
    Парсинг входных данных
    """
    lines = sys.stdin.read().strip().split('\n')
    N, M, S = map(int, lines[0].split(' '))
    lots_by_day = [[] for _ in range(N)]
    for line in lines[1:]:
        package_data = line.split()
        lots_by_day[int(package_data[0]) - 1].append(ObligationPackage(N, *package_data))
    return N, M, S, lots_by_day



def generate_in_day_combinations(lots_by_day):
    """
    Генерирует все возможные комбинации из лотов за день
    :param lots_by_day: лоты, доступные в определённый день
    :return: возможные комбинации предоставленных лотов
    """
    result = []
    for i in range(1, len(lots_by_day) + 1):
        result.extend(itertools.combinations(lots_by_day, i))
    return result


def check_if_combination_can_be_purchased(combination, available_sum):
    """
    Проверяет возможность покупки комбинации
    :param combination: комбинация лотов
    :param available_sum: доступная сумма денег
    :return: возможность покупки, сумма, необходимая для покупки
    """
    purchase_sum = sum([package.ue_price for package in combination])
    return available_sum >= purchase_sum, int(purchase_sum)


def get_combination_income(combination):
    """
    Вычисляет выручку из комбинации
    :param combination: комбинация лотов
    :return: выручка со всех пакетов облигаций в лоте
    """
    return sum([package.full_package_income for package in combination])


def check_last_active_day(buys, current_day, current_money, purchase_sum):
    """
    Проверяет в какой день были совершены покупки для достижения текущей суммы в предыдущие дни
    :param buys: словарь предыдущих возможных покупок
    :param current_day: от какого дня происходит проверка
    :param current_money: текущая сумма денег
    :param purchase_sum: сумма денег для покупки новой комбинации пакетов облигаций
    :return: Покупки в последний день, при котором возможно достичь текущей суммы средств
    """
    prev_day = []
    for day in range(current_day, 0, -1):
        prev_day = buys.get((day, current_money - purchase_sum), [])
        if len(prev_day) > 0:
            break
    return prev_day

def show_max_profit_strategy(dp, buys, N):
    """
    Отображение результатов работы алгоритма
    """
    max_profit = max(dp[N])
    max_money = dp[N].index(max_profit)
    if max_profit <= 0:
        print('Не удалось найти оптимальную стратегию')
    else:
        print(max_profit)
        for key in list(buys.keys())[::-1]:
            if key[1] == max_money:
                for lots_in_day in buys[key]:
                    for lot in lots_in_day:
                        print(lot)
                break
    print()

def get_compiled_combinations_by_day(combinations_by_day, day, current_lots):
    """
    Проверяет наличие уже созданных комбинаций на текущий день и если их нет - добавляет в словарь
    """
    if combinations_by_day.get(day) != None:
        combinations = combinations_by_day[day]
    else:
        combinations = generate_in_day_combinations(current_lots)
        combinations_by_day[day] = combinations
    return combinations_by_day, combinations

def megatrader_dynamic_programming(N, S, lots):
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    buys = {}
    combinations_by_day = {}
    for day in range(1, N + 1):
        current_lots = lots[day - 1]
        for current_money in range(S + 1):
            dp[day][current_money] = max(dp[day][current_money], dp[day - 1][current_money])
            combinations_by_day, combinations = get_compiled_combinations_by_day(combinations_by_day, day, current_lots)
            for combination in combinations:
                can_be_purchased, purchase_sum = check_if_combination_can_be_purchased(combination, current_money)
                if can_be_purchased:
                    new_profit = dp[day - 1][current_money - purchase_sum] + get_combination_income(combination)
                    if new_profit > dp[day][current_money]:
                        dp[day][current_money] = new_profit
                        prev_day = check_last_active_day(buys, day-1, current_money, purchase_sum)
                        buys[(day, current_money)] = prev_day + [combination]
    return dp, buys

def main():
    N, M, S, lots = parse_input()
    dp, buys = megatrader_dynamic_programming(N, S, lots)
    show_max_profit_strategy(dp, buys, N)

if __name__ == '__main__':
    main()
