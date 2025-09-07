def test_class_product(product_1, product_2, property_product_1, property_product_2, new_product):
    assert product_1.name == 'Samsung Galaxy S23 Ultra'
    assert product_1.description == '256GB, Серый цвет, 200MP камера'
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert product_2.name == ''
    assert product_2.description == ''
    assert product_2.price == 0
    assert product_2.quantity == 0

    assert property_product_1.price == 120

    assert property_product_2.price == 300

    assert new_product.name == 'Samsung Galaxy S23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 315
    assert new_product.quantity == 22
