import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def setup_function():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_smartphone_initialization():
    """Тест инициализации Smartphone"""
    smartphone = Smartphone(
        "iPhone", "Смартфон", 100000.0, 5,
        efficiency=3.5, model="15", memory=256, color="Black"
    )

    assert smartphone.name == "iPhone"
    assert smartphone.price == 100000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 3.5
    assert smartphone.model == "15"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_lawn_grass_initialization():
    """Тест инициализации LawnGrass"""
    grass = LawnGrass(
        "Трава", "Газонная", 5000.0, 10,
        country="Россия", germination_period=10, color="Зеленый"
    )

    assert grass.name == "Трава"
    assert grass.price == 5000.0
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == 10
    assert grass.color == "Зеленый"


def test_inheritance():
    """Тест что классы являются наследниками Product"""
    smartphone = Smartphone("Test", "Test", 1000.0, 1, 1.0, "M", 64, "Black")
    grass = LawnGrass("Test", "Test", 1000.0, 1, "RU", 10, "Green")

    assert isinstance(smartphone, Product)
    assert isinstance(grass, Product)
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_addition_same_class():
    """Тест сложения товаров одного класса"""
    smartphone1 = Smartphone("S1", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
    smartphone2 = Smartphone("S2", "Desc", 2000.0, 3, 1.0, "M", 64, "Black")

    result = smartphone1 + smartphone2
    expected = (1000.0 * 2) + (2000.0 * 3)  # 2000 + 6000 = 8000
    assert result == expected


def test_addition_different_classes():
    """Тест что нельзя складывать товары разных классов"""
    smartphone = Smartphone("S", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
    grass = LawnGrass("G", "Desc", 500.0, 4, "RU", 10, "Green")

    with pytest.raises(TypeError) as exc_info:
        _ = smartphone + grass

    assert "Нельзя складывать товары разных классов" in str(exc_info.value)


def test_add_product_with_inherited_classes():
    """Тест что можно добавлять наследников Product в категорию"""
    category = Category("Тест", "Категория")
    smartphone = Smartphone("S", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
    grass = LawnGrass("G", "Desc", 500.0, 4, "RU", 10, "Green")

    category.add_product(smartphone)
    category.add_product(grass)

    assert len(category._products) == 2
    assert Category.product_count == 2


def test_add_product_invalid_type():
    """Тест что нельзя добавлять не-товары в категорию"""
    category = Category("Тест", "Категория")

    with pytest.raises(TypeError) as exc_info:
        category.add_product("не товар")

    assert "Можно добавлять только объекты класса Product или его наследников" in str(exc_info.value)
