import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def setup_function():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_zero_quantity_raises_error():
    """Тест что товар с quantity=0 вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тестовый товар", "Описание", 1000.0, 0)


def test_smartphone_zero_quantity_raises_error():
    """Тест что смартфон с quantity=0 вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Smartphone("Тест", "Описание", 1000.0, 0, 1.0, "M", 64, "Black")


def test_lawn_grass_zero_quantity_raises_error():
    """Тест что газонная трава с quantity=0 вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        LawnGrass("Тест", "Описание", 1000.0, 0, "RU", 10, "Green")


def test_category_average_price_empty():
    """Тест средней цены для пустой категории"""
    category = Category("Пустая категория", "Нет товаров")
    assert category.average_price() == 0


def test_category_average_price_single_product():
    """Тест средней цены для категории с одним товаром"""
    product = Product("Товар", "Описание", 1000.0, 5)
    category = Category("Категория", "Один товар", [product])
    assert category.average_price() == 1000.0


def test_category_average_price_multiple_products():
    """Тест средней цены для категории с несколькими товарами"""
    product1 = Product("Товар1", "Описание", 1000.0, 5)
    product2 = Product("Товар2", "Описание", 2000.0, 3)
    product3 = Product("Товар3", "Описание", 3000.0, 2)

    category = Category("Категория", "Несколько товаров", [product1, product2, product3])

    average_price = category.average_price()
    expected_average = (1000.0 + 2000.0 + 3000.0) / 3
    assert average_price == expected_average
