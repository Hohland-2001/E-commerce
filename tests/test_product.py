def test_class_product(product_1, product_2):
    assert product_1.name == 'Samsung Galaxy S23 Ultra'
    assert product_1.description == '256GB, Серый цвет, 200MP камера'
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert product_2.name == ''
    assert product_2.description == ''
    assert product_2.price == 0
    assert product_2.quantity == 0
