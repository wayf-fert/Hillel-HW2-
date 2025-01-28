def analyze_inheritance(cls) -> None:
    """
    Аналізує спадкування вказаного класу та виводить усі методи, наслідувані від базових класів.

    Args:
        cls (Type): Клас для аналізу.
    """
    inherited_methods: List[str] = []
    for base_class in cls.__bases__:
        for name in dir(base_class):
            if callable(getattr(base_class, name)) and not name.startswith('__'):
                inherited_methods.append(f"{name} з {base_class.__name__}")

    print(f"Клас {cls.__name__} наслідує:")
    if inherited_methods:
        for method in inherited_methods:
            print(f" - {method}")
    else:
        print(" - <немає методів, наслідуваних від базових класів>")


class Parent:
    def parent_method(self) -> None:
        pass


class Child(Parent):
    def child_method(self) -> None:
        pass


analyze_inheritance(Child)
