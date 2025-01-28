class AutoMethodMeta(type):
    """Метаклас для автоматичної генерації геттерів та сеттерів для атрибутів класу."""

    def __new__(cls, name: str, bases, dct: dict):
        """
        Створює новий клас із автоматично згенерованими геттерами та сеттерами.

        Args:
            name (str): Назва класу.
            bases (tuple): Базові класи.
            dct (dict): Атрибути класу.

        Returns:
            Type: Новий клас із геттерами та сеттерами.
        """

        def create_getter(attr_name: str):
            def getter(self):
                return getattr(self, attr_name)

            return getter

        def create_setter(attr_name: str):
            def setter(self, value) -> None:
                setattr(self, attr_name, value)

            return setter

        for attr_name in list(dct.keys()):
            if not attr_name.startswith('__') and not callable(dct[attr_name]):
                getter_name = f'get_{attr_name}'
                setter_name = f'set_{attr_name}'

                dct[getter_name] = create_getter(attr_name)
                dct[setter_name] = create_setter(attr_name)

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    name: str = "John"
    age: int = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
