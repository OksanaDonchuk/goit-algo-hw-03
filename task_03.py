from typing import Dict, List

def hanoi_tower(n: int, source: str, target: str, auxiliary: str, state: Dict[str, List[int]]) -> None:
    """
    Рекурсивно переміщує диски між стрижнями для вирішення задачі Ханойської вежі.

    Args:
        n (int): Кількість дисків для переміщення.
        source (str): Назва стрижня, з якого переміщуються диски.
        target (str): Назва стрижня, на який переміщуються диски.
        auxiliary (str): Назва допоміжного стрижня.
        state (Dict[str, List[int]]): Словник, що зберігає поточний стан стрижнів.
    """
    if n == 1:
        # Переміщуємо один диск
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        state[target].append(state[source].pop())  
        print(f"Проміжний стан: {state}")
    else:
        # Переміщуємо n-1 дисків з source на auxiliary, використовуючи target як допоміжний
        hanoi_tower(n - 1, source, auxiliary, target, state)
        
        # Переміщуємо найбільший диск з source на target
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        state[target].append(state[source].pop()) 
        print(f"Проміжний стан: {state}")
        
        # Переміщуємо n-1 дисків з auxiliary на target, використовуючи source як допоміжний
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main() -> None:
    """
    Запускає програму для розв'язання задачі Ханойської вежі.
    Запитує у користувача кількість дисків та виводить послідовність кроків для переміщення.
    """
    try:
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            raise ValueError("Кількість дисків повинна бути більшою за 0.")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    # Початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Стрижень A містить диски у порядку [n, ..., 2, 1]
        'B': [],  # Стрижень B порожній
        'C': []   # Стрижень C порожній
    }
    
    print(f"Початковий стан: {state}")
    hanoi_tower(n, 'A', 'C', 'B', state)  # Виконуємо алгоритм
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()