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
    def new_product(cls, dict_products: dict = None):
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
    def price(self) -> float:
        """Геттер возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """Сеттер проверят новую заданную цену, и если она меньше или равна 0 - выводит соответствующее сообщение"""
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Магический метод для строкового отображения объекта"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other) -> float:
        """Магический метод для сложения стоимостей товаров"""
        return self.quantity * self.__price + other.quantity * other.__price


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод инициализирует новые характеристики в классе-наследнике"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Переопределения метода сложения для сложения только объектов определенного класса-наследника"""
        if type(other) is Smartphone:
            return super().__add__(other)
        else:
            raise TypeError


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод инициализирует новые характеристики в классе-наследнике"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Переопределения метода сложения для сложения только объектов определенного класса-наследника"""
        if type(other) is LawnGrass:
            return super().__add__(other)
        else:
            raise TypeError
