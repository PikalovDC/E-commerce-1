# Категории и Продукты

Проект для управления категориями товаров и продуктами с автоматическим подсчетом статистики.

## Классы

### Product

Класс для представления товара.

**Атрибуты:**
- `name` (str) - название товара
- `description` (str) - описание товара
- `price` (float) - цена товара (может быть с копейками)
- `quantity` (int) - количество в наличии (в штуках)

**Пример использования:**
from product import Product

# Создание товара
product = Product("Ноутбук", "Мощный игровой ноутбук", 75000.0, 5)

**Магические методы:**
- `__str__` - строковое представление: "Название, цена руб. Остаток: количество шт."
- `__add__` - сложение товаров (только одинаковых классов)

**Методы:**
- `new_product(product_data)` - класс-метод для создания из словаря


### Category
Класс для представления категории товаров.

**Атрибуты экземпляра:**

- name (str) - название категории

- description (str) - описание категории

- products (list[Product]) - список товаров категории

**Атрибуты класса (общая статистика):**

- category_count (int) - общее количество созданных категорий

- product_count (int) - общее количество уникальных товаров

Методы:

- add_product(product) - добавление товара в категорию

**Пример использования:**

from category import Category
from product import Product

# Создание категории
electronics = Category("Электроника", "Товары из мира электроники")

# Создание товаров
laptop = Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)
mouse = Product("Мышь", "Беспроводная мышь", 2500.0, 10)

# Добавление товаров в категорию
electronics.add_product(laptop)
electronics.add_product(mouse)

# Доступ к статистике
print(f"Всего категорий: {Category.category_count}")
print(f"Всего товаров: {Category.product_count}")

### Класс Smartphone (Наследник Product)

**Дополнительные атрибуты:**
- `efficiency` (float) - производительность
- `model` (str) - модель
- `memory` (int) - объем памяти (ГБ)
- `color` (str) - цвет

### Класс LawnGrass (Наследник Product)

**Дополнительные атрибуты:**
- `country` (str) - страна-производитель
- `germination_period` (int) - срок прорастания (дни)
- `color` (str) - цвет

### Наследование и специализированные классы

from src.product import Smartphone, LawnGrass

### Создание смартфона
smartphone = Smartphone(
    "iPhone 15", 
    "Флагманский смартфон", 
    150000.0, 
    5,
    efficiency=3.5, 
    model="15 Pro", 
    memory=256, 
    color="Black"
)

### Создание газонной травы
grass = LawnGrass(
    "Газонная трава Premium", 
    "Высококачественная трава", 
    5000.0, 
    20,
    country="Германия", 
    germination_period=14, 
    color="Зеленый"
)

### Товары можно складывать только если они одного класса:

### Работает - одинаковые классы
smartphone1 = Smartphone("S1", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
smartphone2 = Smartphone("S2", "Desc", 2000.0, 3, 1.0, "M", 64, "Black")
total = smartphone1 + smartphone2  # (1000×2) + (2000×3) = 8000

### Вызывает TypeError - разные классы
smartphone = Smartphone("S", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
grass = LawnGrass("G", "Desc", 500.0, 4, "RU", 10, "Green")
total = smartphone + grass  # TypeError: Нельзя складывать товары разных классов

### Вызывает TypeError - не товар
smartphone = Smartphone("S", "Desc", 1000.0, 2, 1.0, "M", 64, "Black")
total = smartphone + "не товар"  # TypeError: Можно складывать только объекты класса Product

# Тестирование
## Установка Pytest
Если Pytest еще не установлен, установите его с помощью poetry:
`poetry add --group dev pytest`

Запустите тесты используя команду `pytest`

## Структура тестов
Тесты организованы в соответствии со структурой проекта - находятся в папке 'tests'.

## Покрытие тестами
В pytest для анализа покрытия кода надо поставить библиотеку 
pytest-cov:

`# Через poetry с добавлением в отдельную группу
poetry add --group dev pytest-cov`

Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:

+ `pytest --cov` — при активированном виртуальном окружении.
+ `poetry run pytest --cov` — через poetry.
+ `pytest --cov=src --cov-report=html` — чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src — пакет c модулями, которые тестируем. Отчет будет сгенерирован в папке 
htmlcov и храниться в файле с названием index.html
