from typing import Any


class Product:
    """
    Класс для создания экземпляров товара
    """

    # Список всех созданных товаров
    products: list = list()

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.products.append(self)

    def __str__(self) -> str:
        """
        Метод для отображения информации об объекте класса для пользователей
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """
        Метод позволяет складывать только экземпляры одного класса
        """
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError("Объекты разных классов. Сложение невозможно.")

    @property
    def price(self) -> float:
        """
        Метод-геттер, возвращает приватное свойство экземпляра класса - цену на продукт.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Метод-сеттер, устанавливает после проверки значение приватного свойства
        атрибута класса - цены на продукт.
        """
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, arg_dct: dict) -> Any:
        """
        Метод класса, создаёт и возвращает новый экземпляр класса Product, если в списке
        продуктов такого нет, либо преобразует и возвращает уже имеющийся в списке экземпляр.
        """
        if cls.products:
            for elem in cls.products:

                if elem.name == arg_dct["name"]:
                    elem.price = elem.price if elem.price > arg_dct["price"] else arg_dct["price"]
                    elem.quantity += arg_dct["quantity"]

                    return elem

            new_product = cls(*arg_dct.values())

            return new_product
