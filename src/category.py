from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        products (list[Product]): Список товаров категории (объекты класса Product)

    Class Attributes:
        category_count (int): Общее количество категорий
        product_count (int): Общее количество уникальных товаров
    """

    name: str
    description: str
    products: list[Product]

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

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

        # Увеличиваем счетчик категорий
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и увеличивает счетчик уникальных товаров.

        Args:
            product: Объект товара для добавления
        """
        self.products.append(product)
        # Увеличиваем счетчик уникальных товаров при добавлении
        Category.product_count += 1
