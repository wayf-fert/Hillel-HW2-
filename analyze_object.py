def analyze_object(init_obj):
    """Function for parsing any object

    Function for parsing any object.

    Outputs:
        1. Object type.
        2. List of all attributes and methods of the object with their types.

    Arguments:
        obj -- object to parse."""
    print(f"Type object: {type(init_obj)}\n")

    attributes_and_methods = dir(init_obj)
    print("Attributes & methods:\n")

    for name in attributes_and_methods:
        attribute = getattr(obj, name)
        print(f"- {name}: {type(attribute)}")


class MyClass:
    """The class with simple attributes and a method for demonstration."""

    def __init__(self, value: str):
        self.value = value

    def say_hello(self) -> str:
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
