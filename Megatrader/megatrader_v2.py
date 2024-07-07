import sys

def get_package_data(N, line):
    day = int(line[0])
    price = float(line[2])
    quantity = int(line[3])
    bond_income = N - day + 30
    bond_cost = 1000 - price * 10
    return (
        day,
        line[1],
        price,
        quantity,
        int(price * 10 * quantity),
        (bond_cost + bond_income) * quantity,
        bond_cost + bond_income,
    )


def parse_input():
    lines = sys.stdin.read().strip().split("\n")
    N, M, S = map(int, lines[0].split(" "))
    lots = []
    for line in lines[1:]:
        lots.append(get_package_data(N, line.split()))
    return N, M, S, lots


def update_max_profit(max_profit, package, package_id, current_money):
    max_profit[package_id + 1][current_money][0] = (
        max_profit[package_id][current_money - int(package[4])][0] + package[4]
    )
    max_profit[package_id + 1][current_money][1] = (
        max_profit[package_id][current_money - int(package[4])][1] + package[5]
    )
    max_profit[package_id + 1][current_money][2] = max_profit[package_id][
        current_money - int(package[4])
    ][2].copy()
    max_profit[package_id + 1][current_money][2].append(package)
    return max_profit


def reset_max_profit(max_profit, package_id, current_money):
    for item in range(0, 3):
        max_profit[package_id + 1][current_money][item] = max_profit[package_id][current_money][item]
    return max_profit

def show_max_profit(max_profit):
    print(max_profit[-1][-1][1])
    purchased_packages = max_profit[-1][-1][2]
    purchased_packages.sort(key=lambda x: x[0])
    for bond in purchased_packages:
        print(" ".join(map(str, bond[:4])))
    print()

def get_max_profit(S, packages_data):
    max_profit = [
        [[0, 0, []] for _ in range(0, S)] for _ in range(len(packages_data) + 1)
    ]
    packages_data.sort(key=lambda x: x[6], reverse=True)
    for package_id in range(len(packages_data)):
        package = packages_data[package_id]
        for current_sum in range(S):
            item_index = (current_sum + 1) - int(package[4])
            if (
                item_index > 0
                and item_index < len(max_profit[package_id])
                and max_profit[package_id][item_index][0] + package[4] <= (current_sum + 1)
                and max_profit[package_id][item_index][1] + package[5] > max_profit[package_id][current_sum][1]
            ):
                max_profit = update_max_profit(max_profit, package, package_id, current_sum)
            else:
                max_profit = reset_max_profit(max_profit, package_id, current_sum)
    max_profit.sort(key=lambda x: x[0][1])
    return max_profit

def main():
    N, M, S, packages_data = parse_input()
    max_profit = get_max_profit(S, packages_data)
    show_max_profit(max_profit)

if __name__ == "__main__":
    main()
