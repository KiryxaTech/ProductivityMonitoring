class StaticMeta(type):
    """
    Метакласс, который делает все методы внутри класса статическими.
    """
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                setattr(dct[attr_name], '__get__', lambda x: x)
        return super().__new__(cls, name, bases, dct)