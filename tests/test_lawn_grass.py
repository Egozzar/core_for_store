import pytest

from src.product import Product


def test_lawn_grass_init(lawn_grasses_list):
    assert lawn_grasses_list[0].name == "Газонная трава"
    assert lawn_grasses_list[0].description == "Элитная трава для газона"
    assert lawn_grasses_list[0].quantity == 20
    assert lawn_grasses_list[0].price == 500.0
    assert lawn_grasses_list[0].country == "Россия"
    assert lawn_grasses_list[0].germination_period == "7 дней"
    assert lawn_grasses_list[0].color == "Зеленый"


def test_lawn_grass_add(lawn_grasses_list):
    assert lawn_grasses_list[0] + lawn_grasses_list[1] == 16750.0


def test_lawn_grass_wrong(lawn_grasses_list):
    with pytest.raises(TypeError) as err:
        _ = lawn_grasses_list[0] + 1

    assert str(err.value) == "Объекты разных классов. Сложение невозможно."


def test_zeroing():
    Product.products.clear()
