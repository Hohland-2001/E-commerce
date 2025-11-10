from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_list = []
    category_count = 0
    product_count = 0

    def __init__(self, name='', description='', products=None):
        """Метод инициализирует атрибуты"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        if name not in Category.category_list and name != '':
            Category.category_list.append(name)
            Category.category_count = len(Category.category_list)
        Category.product_count += len(products) if products else 0

    def add_product(self, product=''):
        """Метод добавляет продукт в категорию"""
        if isinstance(product, Product) and issubclass(type(product), Product) and product != '':
            self.__products.append(product)
            Category.product_count += 1
            return None
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер возвращает список продуктов"""
        return self.__products

    @property
    def info_product(self):
        """Метод возвращает информацию о продукте"""
        str_ifo_product = ''
        for p in self.__products:
            if p == '':
                continue
            else:
                str_ifo_product += f'{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n'
        return str_ifo_product

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        count = 0
        for product in self.__products:
            count += product.quantity
        return f'{self.name}, количество продуктов: {count} шт.'

    def middle_price(self):
        """Метод считает среднюю цену продуктов в категории"""
        try:
            sum_price = 0
            count = 0
            for p in self.__products:
                sum_price += p.price
                count += 1
            mid_price = sum_price / count
            return mid_price
        except ZeroDivisionError:
            return 0
