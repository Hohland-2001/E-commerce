def test_product_init(product_1, product_2):
    assert product_1.name == 'Samsung Galaxy S23 Ultra'
    assert product_1.description == '256GB, Серый цвет, 200MP камера'
    assert product_1.quantity == 5

    assert product_2.name == ''
    assert product_2.description == ''
    assert product_2.quantity == 0


def test_product_new_product(new_product):
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 315
    assert new_product.quantity == 22


def test_product_price_property(product_1, product_2):
    assert product_1.price == 180000.0
    assert product_2.price == 0


def test_product_price_setter(product_1, product_2):
    product_1.price = 200
    assert product_1.price == 200
    product_1.price = -100
    assert product_1.price == 200
    product_2.price = 300
    assert product_2.price == 300
