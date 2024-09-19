import sqlite3
from abc import ABC, abstractmethod
from dataclasses import dataclass
from sqlite3 import Connection


@dataclass
class AbstractDAO(ABC):
    database: str
    table_name: str = ""
    fields: str = ""

    @abstractmethod
    def __post_init__(self) -> None:
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self) -> Connection:
        return sqlite3.connect(self.database)

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()

    def create(self) -> None:
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.fields}"
        )

    @abstractmethod
    def insert(self, elem: list) -> None:
        pass

    def clear(self) -> None:
        self.cursor.execute(f"DROP TABLE IF EXISTS {self.table_name}")
        self.connection.commit()
