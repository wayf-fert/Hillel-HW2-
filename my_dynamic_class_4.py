def create_class(class_name, self_methods):
    """
    Створює динамічний клас з заданим іменем та методами.

    :param class_name: Ім'я класу
    :param self_methods: Словник, де ключі - це назви методів, а значення - функції
    :return: Створений клас.
    """
    return type(class_name, (object,), self_methods)


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
