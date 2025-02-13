def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для видачі решти.
    Повертає словник із номіналами монет та їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    dp = [float('inf')] * (amount + 1)  # Таблиця для зберігання мінімальної кількості монет
    dp[0] = 0  # Для суми 0 потрібно 0 монет

    # Заповнюємо таблицю dp
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Відновлюємо результат
    result = {}
    remaining_amount = amount
    for coin in sorted(coins, reverse=True):
        if remaining_amount >= coin:
            count = remaining_amount // coin
            result[coin] = count
            remaining_amount -= coin * count

    return result