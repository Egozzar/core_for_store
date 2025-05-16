import pytest

from src.category import Category


def test_catiterator_init(category_iterator):
    assert category_iterator.category.description == "Rich in vitamins and always fresh"
    assert category_iterator.category.name == "Vegetables"


def test_catiterator_iter(category_iterator):
    assert iter(category_iterator).runner == 0


def test_catiterator_next(category_iterator):
    iter(category_iterator)
    assert next(category_iterator) == "Tomato, 250.0 руб. Остаток: 10 шт."
    assert next(category_iterator) == "Pepper, 200.0 руб. Остаток: 15 шт."
    assert next(category_iterator) == "Cucumber, 160.5 руб. Остаток: 20 шт."

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_zeroing():
    Category.category_count = 0
    Category.product_count = 0
