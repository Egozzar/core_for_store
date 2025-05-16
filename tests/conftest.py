import pytest

from src.cat_iterator import CatIterator
from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def category_iterator():
    return CatIterator(
        Category(
            "Vegetables",
            "Rich in vitamins and always fresh",
            [
                Product("Tomato", "Fresh, red, sweet", 250.0, 10),
                Product("Pepper", "Fresh, juicy, sweet", 200.0, 15),
                Product("Cucumber", "Fresh, green, long", 160.5, 20),
            ],
        )
    )


@pytest.fixture
def smatphones_list():
    return [
        Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        ),
        Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"),
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий"),
    ]


@pytest.fixture
def lawn_grasses_list():
    return [
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый"),
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"),
    ]
