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
