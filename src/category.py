from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_list = []
    category_count = 0
    product_count = 0

    def __init__(self, name='', description='', products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        if name not in Category.category_list and name != '':
            Category.category_list.append(name)
            Category.category_count = len(Category.category_list)
        Category.product_count += len(products) if products else 0

    def add_product(self, product=''):
        if isinstance(product, Product) and product != '':
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
            if p == '':
                continue
            else:
                str_ifo_product += f'{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n'
        return str_ifo_product
