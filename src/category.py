from src.product import Product


class Category:
    """
    Класс для представления категории товаров.

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        _products (list[Product]): Приватный список товаров категории

    Class Attributes:
        category_count (int): Общее количество категорий
        product_count (int): Общее количество уникальных товаров
    """

    name: str
    description: str
    _products: list[Product]  # Приватный атрибут

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        """
        Инициализация объекта Category.

        Args:
            name: Название категории
            description: Описание категории
            products: Начальный список товаров (опционально)
        """
        self.name = name
        self.description = description
        self._products = products if products is not None else []

        # Увеличиваем счетчики
        if products:
            # Проверяем что все товары являются Product или его наследниками
            for product in products:
                if not isinstance(product, Product):
                    raise TypeError("Можно добавлять только объекты класса Product или его наследников")
            Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self) -> str:
        """
        Строковое представление категории.

        Returns:
            str: "Название категории, количество продуктов: 200 шт."
        """
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products_count(self) -> int:
        """Количество товаров в этой категории"""
        return len(self._products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию и увеличивает счетчик уникальных товаров.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки.

        Returns:
            str: Строка с перечислением товаров в формате:
                 "Название продукта, 80 руб. Остаток: 15 шт."
        """
        products_list = []
        for product in self._products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            products_list.append(product_info)

        return "\n".join(products_list)
