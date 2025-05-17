from src.product import Product


class LawnGrass(Product):
    """
    Класс для создания экземпляров газонной травы
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра
        с учётом наследования, т.е. вначале инициализируем родительские параметры

        :param country:(str) страна-производитель
        :param germination_period:(str) срок прорастания травы
        :param color:(str) цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
