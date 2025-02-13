import time
from greedy_algorithm import find_coins_greedy
from dynamic_programming import find_min_coins

def get_amount_from_user():
    """
    Запитує у користувача суму для видачі решти.
    Повертає ціле число (суму).
    """
    while True:
        try:
            amount = int(input("Введіть суму для видачі решти: "))
            if amount < 0:
                print("Сума має бути невід'ємним числом. Спробуйте ще раз.")
            else:
                return amount
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def main():
    # Отримуємо суму від користувача
    amount = get_amount_from_user()

    # Жадібний алгоритм
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Алгоритм динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    # Вивід результатів
    print("\nЖадібний алгоритм:")
    print("Результат:", greedy_result)
    print("Час виконання:", greedy_time, "секунд")
    print()

    print("Динамічне програмування:")
    print("Результат:", dp_result)
    print("Час виконання:", dp_time, "секунд")

if __name__ == "__main__":
    main()