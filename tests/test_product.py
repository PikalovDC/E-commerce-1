from unittest.mock import patch

from src.product import Product


def test_price_getter():
    """Тест геттера цены"""
    product = Product("Тест", "Описание", 1000.0, 5)
    assert product.price == 1000.0


def test_price_setter_negative(capfd):
    """Тест сеттера с отрицательной ценой"""
    product = Product("Тест", "Описание", 1000.0, 5)
    product.price = -500.0
    assert product.price == 1000.0  # Цена не изменилась

    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_decrease_confirmation_yes():
    """Тест понижения цены с подтверждением 'y'"""
    product = Product("Тест", "Описание", 1000.0, 5)

    with patch('builtins.input', return_value='y'):
        product.price = 800.0

    assert product.price == 800.0


def test_product_str_method():
    """Тест магического метода __str__ для Product"""
    product = Product("Смартфон", "Хороший телефон", 50000.0, 8)
    expected = "Смартфон, 50000.0 руб. Остаток: 8 шт."
    assert str(product) == expected


def test_product_addition_method():
    """Тест магического метода __add__ для Product"""
    product1 = Product("Товар1", "Описание1", 100.0, 10)
    product2 = Product("Товар2", "Описание2", 200.0, 5)

    result = product1 + product2
    expected = (100.0 * 10) + (200.0 * 5)  # 1000 + 1000 = 2000
    assert result == expected


def test_product_addition_with_itself():
    """Тест сложения продукта с самим собой"""
    product = Product("Товар", "Описание", 150.0, 4)

    result = product + product
    expected = (150.0 * 4) + (150.0 * 4)  # 600 + 600 = 1200
    assert result == expected
