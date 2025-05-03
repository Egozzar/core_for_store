from src.product import Product


class Category:
    """
    Класс для создания категории товара
    """

    # Количество созданных экземпляров данного класса
    category_count: int = 0
    # Количество продуктов, имеющих категорию
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product | None]) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(self.products) if self.products else 0
