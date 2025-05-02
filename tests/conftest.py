import pytest

#from src.category import Category
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
