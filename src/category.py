from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name='', description='', products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
            return None
        else:
            return None

    @property
    def products(self):
        return self.__products

    @property
    def info_product(self):
        str_ifo_product = ''
        for p in self.__products:
            str_ifo_product += f'{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n'
        return str_ifo_product
