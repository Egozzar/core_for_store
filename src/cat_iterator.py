from typing import Any, Iterator

from src.category import Category
from src.product import Product


class CatIterator:
    """
    Шаблон для создания объектов для перебора продуктов одной категории
    """

    def __init__(self, category: Category) -> None:
        """
        Метод для инициализации итератора. Задаем значения атрибутам экземпляра.
        :param category: (Category) экземпляр класса Category
        """
        self.category = category

    def __iter__(self) -> Iterator:
        """
        Метод возвращает итератор класса
        :return: (Iterator)
        """
        self.runner = 0

        return self

    def __next__(self) -> Product | Any:
        """
        Метод возвращает продукт перебираемой категории
        :return: (Product)
        """
        if self.runner < len(self.category.products):
            elem = self.category.products[self.runner]
            self.runner += 1

            return elem

        raise StopIteration
