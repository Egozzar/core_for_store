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

    def add_product(self, product: Product) -> Any:
        """
        Метод добавляет товар класса Product в приватный атрибут - список продуктов
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        """
        Метод-геттер, возвращает приватный атрибут-список продуктов
        в виде списка отформатированных строк
        """
        if self.__products:
            return [f"{elem.name}, {elem.price} руб. Остаток: {elem.quantity} шт." for elem in self.__products]

        return []
