import pytest


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


def test_str(product_1, product_2, new_product):
    assert str(product_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert str(product_2) == ', 0 руб. Остаток: 0 шт.'
    assert str(new_product) == 'Samsung Galaxy S23 Ultra, 315 руб. Остаток: 22 шт.'


def test_add(product_1, product_2, new_product):
    assert product_1 + product_2 == 900000.0
    assert product_1 + new_product == 906930.0
    assert product_2 + new_product == 6930


def test_class_smartphone_init(smart_1):
    assert smart_1.color == 'Серый'
    assert smart_1.efficiency == 95.5
    assert smart_1.model == 'S23 Ultra'
    assert smart_1.memory == 256


def test_class_add(smart_1, smart_2, grass_1):
    assert smart_1 + smart_2 == 2580000.0
    with pytest.raises(TypeError):
        smart_1 + grass_1


def test_class_lawngrass_init(grass_1):
    assert grass_1.country == 'Россия'
    assert grass_1.germination_period == '7 дней'
    assert grass_1.color == 'Зеленый'
