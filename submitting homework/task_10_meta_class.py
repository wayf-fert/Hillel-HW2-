class SingletonMeta(type):
    """Метаклас SingletonMeta, який гарантує, що клас може мати лише один екземпляр."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Метод, який контролює створення екземплярів класу.

        Args:
            *args: Аргументи для ініціалізації класу.
            **kwargs: Іменовані аргументи для ініціалізації класу.

        Returns:
            object: Єдиний екземпляр класу.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        print("Creating instance")

# Створення екземплярів
obj1 = Singleton()  # Creating instance
obj2 = Singleton()

print(obj1 is obj2)  # True
