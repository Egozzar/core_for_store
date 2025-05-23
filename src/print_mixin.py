class PrintMixin:
    """
    Класс-примесь с функционалом вывода в консоль информации
    о экземплярах класса Product и его наследников
    """

    def __init__(self) -> None:
        """
        Метод для инициализации экземпляра класса.
        """
        print(repr(self))

    def __repr__(self) -> str:
        """
        Метод возвращает строковое представление о экземплярах класса Product и его наследников
        """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
