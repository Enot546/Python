import pytest
from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
engine = create_engine(db_connection_string)


@pytest.fixture
def db():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture
def new_company(db):

    sql = text("INSERT INTO company(\"name\") VALUES (:new_name) RETURNING id")
    result = db.execute(sql, {"new_name": "test_company"})
    company_id = result.fetchone()[0]
    print(f"Фикстура: создана компания с id={company_id}")

    yield company_id

    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})
    print(f"Фикстура: удалена компания с id={company_id}")


def test_create_company(db):

    sql = text("INSERT INTO company(\"name\") VALUES (:new_name) RETURNING id")
    result = db.execute(sql, {"new_name": "test_insert"})
    new_id = result.fetchone()[0]

    check = db.execute(
        text("SELECT id, name, description FROM company WHERE id = :id"),
        id=new_id
    ).fetchone()

    assert check is not None, f"Компания с id={new_id} не найдена"
    assert check[1] == "test_insert", f"Имя не совпадает: {check[1]}"
    assert check[2] is None, "Описание должно быть NULL"

    print(f"Компания создана: id={check[0]}, name={check[1]}, description='{check[2]}'")

    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": new_id})
    print(f"Очистка: удалена компания id={new_id}")


def test_update_company(db, new_company):
    company_id = new_company

    db.execute(
        text("UPDATE company SET description = :descr WHERE id = :id"),
        {"descr": "New descr", "id": company_id}
    )

    check = db.execute(
        text("SELECT id, description FROM company WHERE id = :id"),
        id=company_id
    ).fetchone()

    assert check is not None, f"Компания с id={company_id} не найдена"
    assert check[1] == "New descr", f"Описание не обновилось: '{check[1]}'"

    print(f"Описание обновлено: id={check[0]}, description='{check[1]}'")


def test_delete_company(db, new_company):
    company_id = new_company

    check_before = db.execute(
        text("SELECT COUNT(*) FROM company WHERE id = :id"),
        id=company_id
    ).fetchone()
    assert check_before[0] == 1, f"Компания id={
        company_id} должна существовать"
    print(f"До удаления: компания id={company_id} существует")

    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})

    check_after = db.execute(
        text("SELECT COUNT(*) FROM company WHERE id = :id"),
        id=company_id
    ).fetchone()
    assert check_after[0] == 0, f"Компания id={company_id} не удалена!"

    print(f"Компания id={company_id} успешно удалена")
