import pytest


def test_smartphone_init(smatphones_list):
    assert smatphones_list[0].name == "Samsung Galaxy S23 Ultra"
    assert smatphones_list[0].description == "256GB, Серый цвет, 200MP камера"
    assert smatphones_list[0].price == 180000.0
    assert smatphones_list[0].quantity == 5
    assert smatphones_list[0].efficiency == 95.5
    assert smatphones_list[0].model == "S23 Ultra"
    assert smatphones_list[0].memory == 256
    assert smatphones_list[0].color == "Серый"


def test_smartphone_add(smatphones_list):
    assert smatphones_list[0] + smatphones_list[1] == 2580000.0
    assert smatphones_list[0] + smatphones_list[2] == 1334000.0
    assert smatphones_list[2] + smatphones_list[1] == 2114000.0


def test_smartphone_add_wrong(smatphones_list):
    with pytest.raises(TypeError) as err:
        _ = smatphones_list[0] + 1

    assert str(err.value) == "Объекты разных классов. Сложение невозможно."
