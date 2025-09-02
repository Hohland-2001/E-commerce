def test_class_category(category_1, category_2, category_3):
    assert category_1.name == 'Смартфоны'
    assert category_1.description == ('Смартфоны, как средство не только коммуникации, '
                                      'но и получения дополнительных функций для удобства жизни')
    assert category_1.products == [1, 2, 3]

    assert category_2.name == ''
    assert category_2.description == ''
    assert category_2.products == []
    assert category_2.category_count == 2

    assert category_3.name == 't'
    assert category_3.description == 'ooo'
    assert category_3.products == [8, 3, 5, 2]
    assert category_3.product_count == 7
