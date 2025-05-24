from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """
    Абстрактный класс-шаблон для создания необходимой структуры
    класса-наследника
    """

    @abstractmethod
    def __str__(self) -> str:  # pragma: no cover
        """
        Метод определяет строковое представление экземпляров
        классов-наследников
        """
        pass

    @abstractmethod
    def __add__(self, other: Any) -> int | float:  # pragma: no cover
        """
        Метод устанавливает правила сложения экземпляров
        классов-наследников с другими объектами
        :param other: (Any) любой объект
        :return: (int | float) результат сложения
        """
        pass

    @property
    @abstractmethod
    def price(self) -> float:  # pragma: no cover
        """
        Метод-геттер для возврата приватного свойства
        экземпляра класса-наследника
        :return: (float) цена товара
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:  # pragma: no cover
        """
        Метод-сеттер для установки значения приватного свойства
        экземпляра класса-наследника
        :param value: (float) устанавливаемое значение цены товара
        """
        pass
