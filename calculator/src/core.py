def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def get_number(prompt: str) -> float:
    """Функция для безопасного ввода чисел."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")

def calculator():
    """Основной цикл калькулятора."""
    print("--- Простой калькулятор ---")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'выход'")
    
    # Словарь для быстрого сопоставления знака операции с функцией
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        # 1. Выбор операции
        op = input("\nВыберите операцию (+, -, *, /) или 'выход': ").strip().lower()
        
        if op == 'выход':
            print("Программа завершена. До свидания!")
            break
            
        if op not in operations:
            print("Неверная операция! Пожалуйста, выберите +, -, *, или /.")
            continue
            
        # 2. Ввод чисел
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        
        # 3. Вычисление и вывод результата
        try:
            func = operations[op]
            result = func(num1, num2)
            # Форматируем вывод, чтобы не показывать .0 у целых чисел
            print(f"Результат: {num1} {op} {num2} = {result:.4g}")
        except ValueError as e:
            print(f"Ошибка: {e}")

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
