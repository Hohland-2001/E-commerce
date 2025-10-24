import pytest


def test_category_init(category_1, category_2, product_1):
    assert category_1.name == 'Смартфоны'
    assert category_1.description == ('Смартфоны, как средство не только коммуникации, '
                                      'но и получения дополнительных функций для удобства жизни')

    assert category_2.name == ''
    assert category_2.description == ''

    assert category_1.category_count == 1


def test_category_add_product(category_1, product_1, no_product):
    category_1.add_product(product_1)
    assert category_1.product_count == 3
    with pytest.raises(TypeError):
        category_1.add_product(no_product)


def test_category_info_products(category_1):
    assert category_1.info_product == "Samsung, 200.0 руб. Остаток: 10 шт.\n"


def test_str(category_1, category_2, category_info):
    assert str(category_1) == 'Смартфоны, количество продуктов: 10 шт.'
    assert str(category_2) == ', количество продуктов: 0 шт.'
    assert str(category_info) == 'dks, количество продуктов: 27 шт.'
