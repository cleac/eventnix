from enum import IntEnum


class Gender(IntEnum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


class LoginOptions(IntEnum):
    EMAIL = 0
    FACEBOOK = 1


class UserPermissions(IntEnum):
    CAN_REGISTER_ON_EVENTS = 0
    CAN_ORGANIZE_EVENTS = 1


class EventStatus(IntEnum):
    ACTIVE = 0
    CANCELLED = 1


class RegistrationStatus(IntEnum):
    PENDING = 0
    CONFIRMED = 1
    VISITED = 2
    CANCELLED = 3


class FormType(IntEnum):
    REGISTRATION = 0
    FEEDBACK = 1


__all__ = (
    'Gender', 'LoginOptions', 'UserPermissions',
    'EventStatus', 'RegistrationStatus', 'FormType',
)
