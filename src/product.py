class Product:
    """
    Класс для представления продукта.

    Attributes:
        name (str): Название продукта
        description (str): Описание продукта
        price (float): Цена продукта (может быть с копейками)
        quantity (int): Количество в наличии (в штуках)
    """

    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity