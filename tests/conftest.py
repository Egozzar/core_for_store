import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_cucumber():
    return Product("Cucumber", "Fresh, green, long", 160.5, 20)


@pytest.fixture
def category_vegetables():
    return Category(
        "Vegetables",
        "Rich in vitamins and always fresh",
        [
            Product("Tomato", "Fresh, red, sweet", 250.0, 10),
            Product("Pepper", "Fresh, juicy, sweet", 200.0, 15),
            Product("Cucumber", "Fresh, green, long", 160.5, 20),
        ],
    )


@pytest.fixture
def category_fruits():
    return Category(
        "Fruits",
        "Very tasty and very healthy",
        [
            Product("Apple", "Semirenko variety", 220.0, 5),
            Product("Plum", "Variety Renklod", 400.0, 10),
            Product("Banana", "Banana from morocco", 120, 7),
        ],
    )


@pytest.fixture
def category_fruits_empty():
    return Category(
        "Fruits",
        "Very tasty and very healthy",
        [],
    )


@pytest.fixture
def list_object_products():
    return [
        Product("Pepper", "Fresh, juicy, sweet", 200.0, 15),
        Product("Cucumber", "Fresh, green, long", 160.5, 20),
        Product("Apple", "Semirenko variety", 220.0, 5),
    ]


@pytest.fixture
def list_dict_products():
    return [
        {"name": "Potato", "description": "Black-eyed gypsy", "price": 60.0, "quantity": 200},
        {"name": "Cabbage", "description": "Early white cabbage", "price": 125.0, "quantity": 50},
        {"name": "Pineapple", "description": "Wonderful fruit", "price": 400.0, "quantity": 20},
    ]
