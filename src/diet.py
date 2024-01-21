from datetime import datetime
from pathlib import Path
from re import S
from typing import Optional

from sqlalchemy import create_engine, func, null, select
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, Session, mapped_column
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept
from sqlalchemy.types import DateTime, Integer, String


class Base(DeclarativeBase):
    pass


class FoodItem(Base):
    __tablename__ = "FoodItem"

    id: Mapped[int] = mapped_column(
            Integer(),
            primary_key=True,
            nullable=False)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    carbs: Mapped[int] = mapped_column(Integer(), nullable=False)
    fats: Mapped[int] = mapped_column(Integer(), nullable=False)
    protien: Mapped[int] = mapped_column(Integer(), nullable=False)

    def __repr__(self) -> str:
        return (
            f"Food Item(id={self.id!r}, "
            f"name={self.name!r}, "
            f"carbs={self.carbs!r}, "
            f"fats={self.fats!r}, "
            f"protien={self.protien!r})"
        )


def main() -> None:
    db_path = Path("sample_database.db").absolute()
    engine = create_engine(rf"sqlite:///{db_path}")
    Base.metadata.create_all(engine)
    session = Session(engine)
    apple = FoodItem(
            name="apple",
            carbs=10,
            fats=10,
            protien=10)
    session.add(apple)
    session.commit()
    foodItems = session.query(FoodItem).all()

    for row in foodItems:
        print(row)


if __name__ == "__main__":
    main()
