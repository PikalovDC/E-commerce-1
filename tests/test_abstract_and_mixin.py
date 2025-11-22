from abc import ABC

import pytest

from src.abstract_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


def setup_function():
    """Сброс счетчиков перед каждым тестом"""
    from src.category import Category
    Category.category_count = 0
    Category.product_count = 0


def test_base_product_is_abstract():
    """Тест что BaseProduct является абстрактным классом"""
    assert issubclass(BaseProduct, ABC)

    # Нельзя создать экземпляр абстрактного класса
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 1000.0, 5)


def test_product_inherits_from_base_product():
    """Тест что Product наследует от BaseProduct"""
    assert issubclass(Product, BaseProduct)

    # Можно создать экземпляр Product
    product = Product("Тест", "Описание", 1000.0, 5)
    assert isinstance(product, BaseProduct)


def test_smartphone_inherits_from_base_product():
    """Тест что Smartphone наследует от BaseProduct через Product"""
    smartphone = Smartphone("Тест", "Описание", 1000.0, 5, 1.0, "M", 64, "Black")
    assert isinstance(smartphone, BaseProduct)
    assert isinstance(smartphone, Product)


def test_lawn_grass_inherits_from_base_product():
    """Тест что LawnGrass наследует от BaseProduct через Product"""
    grass = LawnGrass("Тест", "Описание", 1000.0, 5, "RU", 10, "Green")
    assert isinstance(grass, BaseProduct)
    assert isinstance(grass, Product)


def test_repr_mixin_functionality(capfd):
    """Тест что ReprMixin выводит сообщение при создании объекта"""
    # Создаем продукт - должен вывести сообщение в консоль
    Product("Тестовый", "Описание", 1000.0, 5)

    captured = capfd.readouterr()
    assert "Создан объект Product" in captured.out
    assert "('Тестовый', 'Описание', 1000.0, 5)" in captured.out


def test_product_repr_method():
    """Тест метода __repr__ для Product"""
    product = Product("Яблоко", "Свежее", 50.0, 10)

    repr_str = repr(product)

    assert repr_str.startswith("Product(")
    assert "name='Яблоко'" in repr_str
    assert "description='Свежее'" in repr_str
    assert "_price=50.0" in repr_str
    assert "quantity=10" in repr_str
    # Проверяем что строки в кавычках, а числа - нет
    assert "'Яблоко'" in repr_str  # строка в кавычках
    assert "50.0" in repr_str  # число без кавычек


def test_smartphone_repr_method():
    """Тест метода __repr__ для Smartphone"""
    smartphone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 3,
        efficiency=3.5, model="15", memory=256, color="Black"
    )

    repr_str = repr(smartphone)

    assert repr_str.startswith("Smartphone(")
    assert "name='iPhone'" in repr_str
    assert "efficiency=3.5" in repr_str
    assert "model='15'" in repr_str
    assert "memory=256" in repr_str
    assert "color='Black'" in repr_str


def test_lawn_grass_repr_method():
    """Тест метода __repr__ для LawnGrass"""
    grass = LawnGrass(
        "Трава", "Газонная", 5000.0, 20,
        country="Германия", germination_period=14, color="Зеленый"
    )

    repr_str = repr(grass)

    assert repr_str.startswith("LawnGrass(")
    assert "name='Трава'" in repr_str
    assert "country='Германия'" in repr_str
    assert "germination_period=14" in repr_str
    assert "color='Зеленый'" in repr_str


def test_multiple_objects_creation_logging(capfd):
    """Тест логирования создания нескольких объектов"""
    Product("Товар1", "Описание1", 1000.0, 5)
    Product("Товар2", "Описание2", 2000.0, 3)
    Smartphone("Смартфон", "Техника", 50000.0, 2, 1.0, "M", 64, "Black")

    captured = capfd.readouterr()
    lines = captured.out.strip().split('\n')

    # Должно быть 3 сообщения о создании
    assert len(lines) == 3
    assert "Создан объект Product" in lines[0]
    assert "Создан объект Product" in lines[1]
    assert "Создан объект Smartphone" in lines[2]
