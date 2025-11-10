from src.category import Category
from src.product import Product


def setup_function():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    """Тест корректности инициализации объектов класса Product"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_product_with_fractional_price():
    """Тест создания продукта с дробной ценой"""
    product = Product("Книга", "Учебник", 1500.99, 5)

    assert product.price == 1500.99
    assert isinstance(product.price, float)


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    product = Product("Товар", "Описание", 1000.0, 0)

    assert product.quantity == 0
    assert isinstance(product.quantity, int)


def test_category_initialization():
    """Тест корректности инициализации объектов класса Category"""
    category = Category("Электроника", "Технические товары")

    assert category.name == "Электроника"
    assert category.description == "Технические товары"
    assert category.products == []


def test_category_count_increment():
    """Тест подсчета количества категорий"""
    assert Category.category_count == 0

    category1 = Category("Категория 1", "Описание 1")
    assert Category.category_count == 1

    category2 = Category("Категория 2", "Описание 2")
    assert Category.category_count == 2

    category3 = Category("Категория 3", "Описание 3")
    assert Category.category_count == 3


def test_product_count_increment():
    """Тест подсчета количества уникальных продуктов"""
    assert Category.product_count == 0

    category = Category("Тестовая", "Категория для теста")
    product1 = Product("Товар 1", "Описание 1", 1000.0, 5)
    product2 = Product("Товар 2", "Описание 2", 2000.0, 3)
    product3 = Product("Товар 3", "Описание 3", 3000.0, 7)

    category.add_product(product1)
    assert Category.product_count == 1

    category.add_product(product2)
    assert Category.product_count == 2

    category.add_product(product3)
    assert Category.product_count == 3


def test_add_product_to_category():
    """Тест добавления продуктов в категорию"""
    category = Category("Одежда", "Модная одежда")
    product1 = Product("Футболка", "Хлопковая футболка", 1500.0, 20)
    product2 = Product("Джинсы", "Синие джинсы", 5000.0, 15)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2
    assert product1 in category.products
    assert product2 in category.products
    assert category.products[0].name == "Футболка"
    assert category.products[1].price == 5000.0


def test_multiple_categories_products_count():
    """Тест подсчета продуктов при нескольких категориях"""
    electronics = Category("Электроника", "Техника")
    books = Category("Книги", "Литература")

    laptop = Product("Ноутбук", "Игровой", 75000.0, 5)
    phone = Product("Телефон", "Смартфон", 50000.0, 10)
    book1 = Product("Книга 1", "Роман", 1500.0, 20)
    book2 = Product("Книга 2", "Детектив", 2000.0, 15)

    electronics.add_product(laptop)
    electronics.add_product(phone)
    books.add_product(book1)
    books.add_product(book2)

    assert Category.category_count == 2
    assert Category.product_count == 4
    assert len(electronics.products) == 2
    assert len(books.products) == 2
