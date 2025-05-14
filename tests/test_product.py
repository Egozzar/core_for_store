from src.product import Product


def test_product_init(product_cucumber):
    assert product_cucumber.name == "Cucumber"
    assert product_cucumber.description == "Fresh, green, long"
    assert product_cucumber.price == 160.5
    assert product_cucumber.quantity == 20
    assert len(Product.products) == 1
    Product.products.clear()


def test_price_get_property(list_object_products):
    assert list_object_products[0].price == 200.0
    assert list_object_products[1].price == 160.5
    assert list_object_products[2].price == 220.0
    Product.products.clear()


def test_price_set_property(list_object_products, capsys):
    list_object_products[0].price = 115.2
    assert list_object_products[0].price == 115.2

    list_object_products[0].price = 0.0
    captured = capsys.readouterr()

    assert list_object_products[1].price == 160.5
    assert captured.out[:-1] == "Цена не должна быть нулевая или отрицательная"

    list_object_products[0].price = -200.5
    captured = capsys.readouterr()

    assert list_object_products[2].price == 220.0
    assert captured.out[:-1] == "Цена не должна быть нулевая или отрицательная"


def test_new_product(list_dict_products):
    Product.products.clear()
    prod = Product("Apricot", "Sun of Uzbekistan", 500.0, 50)
    assert len(Product.products) == 1

    assert Product.new_product(list_dict_products[2]).quantity == 20
    assert len(Product.products) == 2

    Product.new_product({"name": "Apricot", "description": "Sun of Uzbekistan", "price": 550.5, "quantity": 70})
    assert len(Product.products) == 2
    assert prod.name == "Apricot"
    assert prod.price == 550.5
    assert prod.quantity == 120


def test_product_str(product_cucumber):
    assert str(product_cucumber) == "Cucumber, 160.5 руб. Остаток: 20 шт."


def test_product_add(list_object_products):
    assert list_object_products[0] + list_object_products[1] == 6210.0
