from datetime import datetime

from eventnix.storage.enumerates import (
    Gender, LoginOptions, UserPermissions,
    EventStatus, RegistrationStatus, FormType,
)
from eventnix.storage.types import TypeEnum
from sqlalchemy import (
    Integer, Text, String, ForeignKey, Column, Table, DateTime, MetaData,
)
from sqlalchemy.dialects.postgres import (
    ARRAY, JSONB, UUID,
)

metadata = MetaData()

tb_user = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('email', Text, unique=True, nullable=False),
    Column('login_options', ARRAY(TypeEnum(LoginOptions))),  # how user log in
    Column('digest', String(64)),  # We'll use SHA-256
    Column('salt', String(64)),
    Column('first_name', Text, nullable=False),
    Column('last_name', Text),
    Column('age', Integer),
    Column('gender', TypeEnum(Gender), default=Gender.UNKNOWN),
    Column('permissions', ARRAY(TypeEnum(UserPermissions))),
    Column('facebook_token', Text),
    Column('unique_identifier', Text, unique=True),
)

tb_event = Table(
    'events', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', Text, nullable=False),
    Column('description', Text),
    Column('organizer_id', Integer, ForeignKey('users.id'),
           nullable=False),
    Column('location', JSONB),
    Column('datetime', DateTime(timezone=True)),
    Column('status', TypeEnum(EventStatus), nullable=False,
           default=EventStatus.ACTIVE),
    Column('max_registrations', Integer, nullable=True),
    Column('registration_form_id', Integer, ForeignKey('forms.id'),
           nullable=True),
    Column('feedback_form_id', Integer, ForeignKey('forms.id'),
           nullable=True),
    Column('logo_id', Integer, ForeignKey('images.id'), nullable=True),
)

tb_registration = Table(
    'registrations', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('event_id', Integer, ForeignKey('events.id'),
           nullable=False),
    Column('status', TypeEnum(RegistrationStatus), nullable=False,
           default=RegistrationStatus.PENDING),
    Column('timestamp', DateTime(timezone=True), nullable=False,
           default=datetime.now()),
    Column('additional_info', JSONB, nullable=True),
)

tb_image = Table(
    'images', metadata,
    Column('id', Integer, primary_key=True),
    Column('filename', UUID, unique=True),
    Column('extension', String(10), nullable=False),
)

tb_form = Table(
    'forms', metadata,
    Column('id', Integer, primary_key=True),
    Column('type', TypeEnum(FormType), nullable=False,
           default=FormType.REGISTRATION),
    Column('description', Integer, nullable=True),
    Column('fields', JSONB, nullable=False),
)

__all__ = (
    'metadata', 'tb_user', 'tb_event', 'tb_form', 'tb_image',
    'tb_registration',
)
