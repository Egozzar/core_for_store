def test_category(category_vegetables, category_fruits):
    assert category_vegetables.name == "Vegetables"
    assert category_vegetables.description == "Rich in vitamins and always fresh"
    assert len(category_vegetables.products) == 3

    assert category_fruits.category_count == 2
    assert category_vegetables.product_count == 6
