import pytest

from src.category import Category
from src.product import Product


def test_add_product_wrong(category_vegetables):
    Category.category_count = 0
    Category.product_count = 0

    with pytest.raises(TypeError) as err:
        category_vegetables.add_product(1)

    assert str(err.value) == "Добавление объекта невозможно."
    assert category_vegetables.product_count == 0


def test_category(category_vegetables, category_fruits):

    assert category_vegetables.name == "Vegetables"
    assert category_vegetables.description == "Rich in vitamins and always fresh"
    assert len(category_vegetables.products) == 3

    assert category_fruits.category_count == 2
    assert category_vegetables.product_count == 6


def test_add_product(category_vegetables, product_cucumber):
    Category.category_count = 0
    Category.product_count = 0

    category_vegetables.add_product(product_cucumber)
    assert category_vegetables.product_count == 1


def test_products_get_property(category_fruits):
    assert category_fruits.products[0] == "Apple, 220.0 руб. Остаток: 5 шт."


def test_products_get_property_empty(category_fruits_empty):
    assert category_fruits_empty.products == []
    Product.products.clear()


def test_category_str(category_fruits):
    assert str(category_fruits) == "Fruits, количество продуктов: 22 шт."


def test_category_middle_price(category_fruits):
    assert category_fruits.middle_price() == 246.67


def test_category_middle_price_empty(category_fruits_empty):
    assert category_fruits_empty.middle_price() == 0


def test_zeroing():
    Product.products.clear()
