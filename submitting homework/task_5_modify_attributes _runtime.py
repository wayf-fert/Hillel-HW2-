def create_class(class_name: str, methods: dict) -> type:
    """
    Динамічно створює клас з заданим іменем та методами.

    Args:
        class_name (str): Назва класу.
        methods (dict): Словник методів, де ключі — назви методів, а значення — функції.

    Returns:
        type: Динамічно створений клас.
    """
    return type(class_name, (object,), methods)


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
