from enum import Enum

from sqlalchemy.types import TypeDecorator
from sqlalchemy import SmallInteger


class TypeEnum(TypeDecorator):
    """
    Matches Integer values with named IntEnums
    """

    impl = SmallInteger

    def __init__(self, enum, *args, **kwargs):
        self._enum = enum
        super().__init__(*args, **kwargs)

    def python_type(self):
        return self._enum

    def process_bind_param(self, value, dialect):
        if isinstance(value, Enum):
            return value.value
        elif isinstance(value, int):
            try:
                self._enum(value)
            except ValueError as ve:
                raise TypeError(
                    'cannot use value {} with enum \'{}\''
                    .format(value, self._enum.__name__)
                ) from ve
            else:
                return value
        return None

    def process_literal_param(self, value, dialect):
        return self._enum(value)

    def process_result_value(self, value, dialect):
        return self._enum(value)


__all__ = ('TypeEnum',)
