class ReprMixin:
    """
    Миксин для логирования создания объектов.
    Печатает информацию о создании объекта в консоль.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__}{args}")

    def __repr__(self) -> str:
        attributes = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                attributes.append(f"{key}='{value}'")
            else:
                attributes.append(f"{key}={value}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"
