import pytest
from src.product import Product
from src.category import Category


@pytest.fixture()
def product_1():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_2():
    return Product()


@pytest.fixture()
def category_1():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [1, 2, 3])


@pytest.fixture()
def category_2():
    return Category()


@pytest.fixture()
def category_3():
    return Category("t",
                    "ooo",
                    [8, 3, 5, 2])
