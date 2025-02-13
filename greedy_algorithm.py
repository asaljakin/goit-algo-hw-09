def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    Повертає словник із кількістю монет кожного номіналу.
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    result = {}  # Словник для зберігання результату

    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Кількість монет поточного номіналу
            result[coin] = count
            amount -= coin * count  # Зменшуємо суму на видану кількість монет

    return result