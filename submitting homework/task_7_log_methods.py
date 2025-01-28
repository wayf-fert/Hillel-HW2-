def log_methods(cls):
    """
    Декоратор, який логуватиме виклики всіх методів класу.

    Args:
        cls (Type): Клас, методи якого потрібно обгорнути.

    Returns:
        Type: Клас із логуванням методів.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):  # Перевіряємо, чи це метод
            original_method = attr_value

            def wrapper(self, *args, **kwargs):
                print(f"Logging: {attr_name} called with {args} {kwargs}")
                return original_method(self, *args, **kwargs)

            wrapper.__annotations__ = original_method.__annotations__

            setattr(cls, attr_name, wrapper)

    return cls


@log_methods
class MyClass:
    def add(self, a: int, b: int) -> int:
        """
        Додавання 2х чисел

        Args:
            a (int): Перше число.
            b (int): Друге число.

        Returns:
            int: Результат додавання.
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Віднімання 2х чисел.

        Args:
            a (int): Зменшуване число.
            b (int): Від'ємник.

        Returns:
            int: Результат віднімання.
        """
        return a - b


obj = MyClass()
print(obj.add(5, 3))  # Logging: add called with (5, 3) {}
print(obj.subtract(5, 3))  # Logging: subtract called with (5, 3) {}
