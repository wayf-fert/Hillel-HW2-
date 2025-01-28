class DynamicProperties:
    """Клас, який дозволяє динамічно додавати властивості з геттерами та сеттерами."""

    def add_property(self, name: str, default_value: any) -> None:
        """
        Додає властивість з геттером та сеттером.

        Args:
            name (str): Назва властивості.
            default_value (any): Початкове значення властивості.
        """
        private_name = f"_{name}"

        def getter(self) -> any:
            return getattr(self, private_name, default_value)

        def setter(self, value: any) -> None:
            setattr(self, private_name, value)

        setattr(type(self), name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
