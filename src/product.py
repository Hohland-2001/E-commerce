class Product:
    name: str
    description: str
    price: float
    quantity: int
    list_products: list

    def __init__(self, name='', description='', price=0, quantity=0):
        """Метод инициализирует атрибуты"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_products=None):
        """Метод принимает на вход словарь и соответственно присваивает каждому атрибуту значение"""
        if dict_products is not None:
            name = dict_products["name"]
            description = dict_products["description"]
            price = dict_products["price"]
            quantity = dict_products["quantity"]
            return cls(name, description, price, quantity)
        else:
            return None

    @property
    def price(self):
        """Геттер возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер проверят новую заданную цену, и если она меньше или равна 0 - выводит соответствующее сообщение"""
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price
        return None

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Магический метод для сложения стоимостей товаров"""
        return self.quantity * self.__price + other.quantity * other.__price
