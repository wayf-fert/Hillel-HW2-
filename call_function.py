def call_function(obj, method_name: str, a: float, b: float):
    """
    Викликає метод об'єкта за його назвою.

    Параметри:
        obj (object): Об'єкт, метод якого потрібно викликати.
        method_name (str): Назва методу у вигляді рядка.

    Return:
        Результат виконання методу.

    Func getattr:
        Використовується для отримання атрибута об'єкта obj за назвою, переданою method_name

    :argument None:
        якщо атрибут за назвою не знайдений в об'єкті obj. Запобігає виникненню помилки AttributeError.

    raise ValueError:
        Якщо метод не знайдено(method = None), викликає - виключення ValueError, щоб повідомити про це.
"""

    method = getattr(obj, method_name, None)

    if method is None:
        raise ValueError(f"Method '{method_name}' not find.")
    return method(a, b)


class Calculator:
    def __init__(self):
        """
        Конструктор класу Calculator.
        """
        pass

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Додає два числа.

        Param:
            a (float): Перше число.
            b (float): Друге число.

        Return:
            float: Сума чисел a та b.
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Віднімає друге число від першого.

        Param:
            a (float): Перше число.
            b (float): Друге число.

        Return:
            float: Різниця чисел a та b.
        """
        return a - b


calc = Calculator()

while True:
    calc = Calculator()

    # Отримання чисел від користувача
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

    print(f'\nAdding: {call_function(calc, 'add', first_num, second_num)}')
    print(f'\nSubtraction: {call_function(calc, "subtract", first_num, second_num)}\n')

    choice = input("Do you want to end this program? (y/n): ").strip().lower()
    if choice == 'y':
        print("Програма завершена.")
        exit()
