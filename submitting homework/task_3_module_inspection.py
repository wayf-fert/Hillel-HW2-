import inspect
import importlib.util


def module_inspection(module_name: str) -> None:
    """
    Аналізує вказаний модуль і виводить список усіх класів, функцій та їхніх сигнатур.

    Args:
        module_name (str): Назва модуля для аналізу.
    """
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"Модуль '{module_name}' не знайдено.")
        return

    module = importlib.import_module(module_name)

    functions = []
    classes = []

    for name, member in inspect.getmembers(module):
        if callable(member) and not inspect.isclass(member):
            try:
                sig = inspect.signature(member)
                functions.append(f"{name}{sig}")
            except ValueError:
                functions.append(f"{name}(<signature недоступна>)")
        elif inspect.isclass(member):
            methods = [
                f"{m_name}{inspect.signature(m_member)}"
                for m_name, m_member in inspect.getmembers(member)
                if callable(m_member)
            ]
            classes.append(f"Клас {name}:\n  Методи:\n    {', '.join(methods)}")

    if functions:
        print("Функції:")
        for func in functions:
            print(f" - {func}")
    else:
        print("Функції: <немає функцій у модулі>")

    if classes:
        print("\nКласи:")
        for cls in classes:
            print(f" - {cls}")
    else:
        print("Класи: <немає класів у модулі>")


module_name = input("Введіть назву модуля: ")
module_inspection(module_name)
