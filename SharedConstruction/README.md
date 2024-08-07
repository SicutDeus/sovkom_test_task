# Долевое строительство
Дан набор из N долей, представленных в виде N рациональных. Необходимо
представить эти доли в процентном выражении c точностью до трех знаков после
запятой.

#### Входные данные
Первая строка содержит значение N - число долей, каждая последующая содержит
числовое выражение доли.
```
4
1.5
3
6
1.5
```

#### Выходные данные
N строк с процентным выражением долей. Значение в строке k является процентным
выражение доли из строки k+1 входных данных
```
0.125
0.250
0.500
0.125
```

### Анализ программы
#### 1. Вычислительная сложность алгоритма и оценка необходимой памяти

**Вычислительная сложность:**

- **Функция `convert_to_percentage`:**
  - Сложность вычисления суммы всех элементов списка: O(N), где N — количество элементов в списке `shares`.
  - Сложность деления каждого элемента списка на общую сумму и форматирования строки: O(N).

  Итого, сложность функции `convert_to_percentage`: O(2N) == O(N).

- **Функция `parse_share`:**
  - Сложность проверки, является ли строка числом: (O(1)).
  - Сложность преобразования строки в число: (O(1)).

  Итого, сложность функции `parse_share`: O(1).

- **Функция `shared_construction`:**
  - Чтение данных из `stdin` и разделение на значение: O(M), где M — количество символов во входных данных.
  - Преобразование первого элемента в целое число: O(1).
  - Обработка всех долей с использованием функции `parse_share`: O(N), где N — количество долей.
  - Вызов функции `convert_to_percentage`, как уже определили: O(N).

  Итого, сложность функции `shared_construction`: O(M + N) == O(N).

**Оценка необходимой памяти:**

- Список `data`: O(M).
- Список `shares`: O(N).
- Список `percentages`: O(N).

Итого, необходимая память: O(N).

#### 2. Ограничения на размер входных параметров

Для того чтобы программа выполнялась в разумное время (до 5 секунд), максимально допустимый размер входных данных:

- Сложность алгоритма: O(N).
- Предположим, что обработка одного элемента занимает приблизительно 10^{-6} секунд.

Максимально допустимое N: N ≤ 5 / (10^(-6)) => N ≤ 5 * 10^(6)

То есть, программа для данного N будет выполняться менее 5с (без учёта аппаратной составляющей).

#### 3. Субъективная оценка сложности задачи

- **Субъективная оценка сложности задачи по шкале от 1 до 10:**
  - **1** 

- **Затраченное время:**
  - 7-10 минут
