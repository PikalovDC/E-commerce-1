from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        products (list[Product]): Список товаров категории (объекты класса Product)
    """

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str) -> None:
        """
        Инициализация объекта Category.

        Args:
            name: Название категории
            description: Описание категории
        """
        self.name = name
        self.description = description
        self.products = []