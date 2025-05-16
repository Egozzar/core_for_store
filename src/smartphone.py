from src.product import Product


class Smartphone(Product):
    """
    Класс для создания экземпляров смартфонов
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра
        с учётом наследования, т.е. вначале инициализируем родительские параметры

        :param efficiency: (float) производительность
        :param model: (str) название модели
        :param memory: (int) объём встроенной памяти
        :param color: (str) цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
