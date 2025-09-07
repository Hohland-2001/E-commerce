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
def property_product_1():
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 120, 14)
    product3.price = 0
    return product3


@pytest.fixture()
def property_product_2():
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 120, 14)
    product3.price = 300
    return product3


@pytest.fixture()
def new_product():
    return Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 315,
         "quantity": 22})


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


@pytest.fixture()
def category_info():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("dks", "iej", [product1, product2, product3])
