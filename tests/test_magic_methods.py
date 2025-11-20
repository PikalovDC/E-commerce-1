import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


def setup_function():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_str_representation():
    """Тест строкового представления Product"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_category_str_representation():
    """Тест строкового представления Category"""
    product1 = Product("Товар1", "Описание", 1000.0, 3)
    product2 = Product("Товар2", "Описание", 2000.0, 2)
    category = Category("Тестовая", "Категория", [product1, product2])

    expected = "Тестовая, количество продуктов: 5 шт."
    assert str(category) == expected


def test_category_str_with_empty_products():
    """Тест строкового представления Category без товаров"""
    category = Category("Пустая", "Категория")
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(category) == expected


def test_category_str_calculates_total_quantity():
    """Тест что Category.__str__ правильно считает общее количество"""
    product1 = Product("Товар1", "Описание", 1000.0, 5)
    product2 = Product("Товар2", "Описание", 2000.0, 3)
    product3 = Product("Товар3", "Описание", 3000.0, 2)
    category = Category("Тестовая", "Категория", [product1, product2, product3])

    # 5 + 3 + 2 = 10
    expected = "Тестовая, количество продуктов: 10 шт."
    assert str(category) == expected


def test_product_addition():
    """Тест сложения продуктов"""
    product_a = Product("Товар A", "Описание A", 100.0, 10)
    product_b = Product("Товар B", "Описание B", 200.0, 2)

    result = product_a + product_b
    expected = (100.0 * 10) + (200.0 * 2)  # 1000 + 400 = 1400
    assert result == expected


def test_product_addition_with_different_prices():
    """Тест сложения продуктов с разными ценами и количествами"""
    product1 = Product("Книга", "Учебник", 1500.0, 3)
    product2 = Product("Ручка", "Шариковая", 50.0, 20)

    result = product1 + product2
    expected = (1500.0 * 3) + (50.0 * 20)  # 4500 + 1000 = 5500
    assert result == expected


def test_addition_same_base_class_but_different():
    """Тест что даже наследники Product не складываются между собой"""
    smartphone = Smartphone("S", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
    grass = LawnGrass("G", "Desc", 500.0, 4, "RU", 10, "Green")
    product = Product("P", "Desc", 300.0, 5)

    # Нельзя складывать разные классы, даже если они наследники Product
    with pytest.raises(TypeError):
        _ = smartphone + grass

    with pytest.raises(TypeError):
        _ = smartphone + product

    with pytest.raises(TypeError):
        _ = grass + product


def test_product_addition_with_zero_quantity():
    """Тест сложения продуктов с нулевым количеством"""
    product1 = Product("Товар1", "Описание", 1000.0, 0)
    product2 = Product("Товар2", "Описание", 2000.0, 5)

    result = product1 + product2
    expected = (1000.0 * 0) + (2000.0 * 5)  # 0 + 10000 = 10000
    assert result == expected


def test_product_addition_with_itself():
    """Тест сложения продукта с самим собой"""
    product = Product("Товар", "Описание", 150.0, 4)

    result = product + product
    expected = (150.0 * 4) + (150.0 * 4)  # 600 + 600 = 1200
    assert result == expected


def test_category_products_uses_product_str():
    """Тест что property products использует __str__ продуктов"""
    product = Product("Тест", "Описание", 1000.0, 5)
    category = Category("Тестовая", "Категория", [product])

    products_str = category.products
    expected_product_str = "Тест, 1000.0 руб. Остаток: 5 шт."
    assert expected_product_str in products_str


def test_product_str_format():
    """Тест точного формата строкового представления Product"""
    product = Product("Точный тест", "Описание", 1234.56, 7)
    result = str(product)

    assert result.startswith("Точный тест, ")
    assert "1234.56 руб." in result
    assert "Остаток: 7 шт." in result
    assert result == "Точный тест, 1234.56 руб. Остаток: 7 шт."
