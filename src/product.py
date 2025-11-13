class Product:
    """
    Класс для представления продукта.

    Attributes:
        name (str): Название продукта
        description (str): Описание продукта
        _price (float): Приватная цена продукта (может быть с копейками)
        quantity (int): Количество в наличии (в штуках)
    """

    name: str
    description: str
    _price: float  # Приватный атрибут цены
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Product.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self._price = price  # Устанавливаем через приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер для получения цены продукта.
        """
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для установки цены продукта с проверкой.

        Аргументы:
            new_price: Новая цена продукта
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            # Не устанавливаем новую цену, оставляем старую
        elif new_price < self._price:
            # Если цена понижается, запрашиваем подтверждение
            print(f"Внимание! Цена понижается с {self._price} до {new_price}")
            confirmation = input("Подтвердите понижение цены (y - да, любой другой символ - нет): ")
            if confirmation.lower() == 'y':
                self._price = new_price
                print("Цена успешно понижена")
            else:
                print("Изменение цены отменено")
        else:
            # Если цена повышается или остается той же, устанавливаем без подтверждения
            self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """
        Класс-метод для создания объекта Product из словаря.

        Args:
            product_data (dict): Словарь с данными товара. Должен содержать ключи:
                - 'name': название товара
                - 'description': описание товара
                - 'price': цена товара
                - 'quantity': количество товара

        Возвращает:
            Product: Созданный объект класса Product

        Raises:
            ValueError: Если в словаре отсутствуют обязательные ключи
        """
        # Проверяем наличие обязательных полей
        required_fields = ['name', 'description', 'price', 'quantity']
        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        # Извлекаем данные из словаря
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        # Создаем и возвращаем объект Product
        return cls(name, description, price, quantity)
