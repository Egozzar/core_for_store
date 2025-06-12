from functools import reduce
from typing import Any

from src.product import Product


class Category:
    """
    Класс для создания категории товара
    """

    # Количество созданных экземпляров данного класса
    category_count: int = 0
    # Количество продуктов, имеющих категорию
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products) if self.__products else 0

    def __str__(self) -> str:
        """
        Метод для отображения информации об объекте класса для пользователей
        """
        total_quant = reduce(lambda summ, elem: summ + elem.quantity, self.__products, 0)

        return f"{self.name}, количество продуктов: {total_quant} шт."

    def add_product(self, product: Product) -> Any:
        """
        Метод добавляет только товары класса Product и его наследников
        в приватный атрибут - список продуктов
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавление объекта невозможно.")

    @property
    def products(self) -> list:
        """
        Метод-геттер, возвращает приватный атрибут-список продуктов
        в виде списка отформатированных строк
        """
        if self.__products:
            return [str(elem) for elem in self.__products]

        return []

    def middle_price(self) -> float | int:
        """
        Метод возвращает среднее значение цены товаров категории
        """
        try:
            if not self.products:
                raise ValueError

            average_price = sum([elem.price for elem in self.__products]) / len(self.__products)
            return round(average_price, 2)

        except ValueError:
            return 0
