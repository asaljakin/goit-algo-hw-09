# Порівняння жадібного алгоритму та динамічного програмування

## Жадібний алгоритм
- **Переваги**: Швидкий, простий у реалізації.
- **Недоліки**: Не завжди знаходить оптимальне рішення.
- **Часова складність**: O(n), де n — кількість номіналів монет.

## Динамічне програмування
- **Переваги**: Завжди знаходить оптимальне рішення.
- **Недоліки**: Вимагає більше пам'яті та часу для великих сум.
- **Часова складність**: O(amount * n), де amount — задана сума, а n — кількість номіналів монет.

## Висновки
- Для малих сум обидва алгоритми працюють швидко, але жадібний алгоритм простіший.
- Для великих сум алгоритм динамічного програмування є більш надійним, оскільки завжди знаходить оптимальне рішення.
- Жадібний алгоритм може бути менш ефективним для певних наборів монет.