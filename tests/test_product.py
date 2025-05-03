def test_product_init(product_cucumber):
    assert product_cucumber.name == "Cucumber"
    assert product_cucumber.description == "Fresh, green, long"
    assert product_cucumber.price == 160.5
    assert product_cucumber.quantity == 20
