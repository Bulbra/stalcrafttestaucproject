from datetime import datetime

from sqlalchemy import Column, Integer, String, \
    BOOLEAN, Text, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


