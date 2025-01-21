class Proxy:
    """
    Клас Proxy переадресовує виклики методів цільового об'єкта,
    додаючи логування викликів методів із аргументами.
    """
    def __init__(self, target: object):
        """
        Ініціалізує Proxy із заданим цільовим об'єктом.
        :param target: Об'єкт, методи якого потрібно перехоплювати.
        """
        self._target = target

    def __getattr__(self, name: str):
        """
        Перехоплює доступ до атрибутів та методів цільового об'єкта.
        :param name: Ім'я методу.
        :return: Логований метод
        """
        attr = getattr(self._target, name)
        if callable(attr):
            return lambda *a, **kw: (print(f"Method {name}(): with args: {a}"), attr(*a, **kw))[1]
        return attr

class MyClass:
    """
    Клас із статичним методом greet().
    """
    @staticmethod
    def greet(name: str) -> str:
        """
        Вітання користувача за іменем.
        :param name: Ім'я користувача.
        :return: Строка вітання.
        """
        return f"Hello, {name}!"

obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))

