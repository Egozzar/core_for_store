from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_init(capsys):
    _ = Product("Cucumber", "Fresh, green, long", 160.5, 20)
    captured = capsys.readouterr()

    assert captured.out.strip() == "Product(Cucumber, Fresh, green, long, 160.5, 20)"
    Product.products.clear()


def test_smartphone_init(capsys):
    _ = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    captured = capsys.readouterr()

    assert captured.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    Product.products.clear()


def test_lawn_grass_init(capsys):
    _ = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    captured = capsys.readouterr()

    assert captured.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    Product.products.clear()
