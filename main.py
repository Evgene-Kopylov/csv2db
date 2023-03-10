from models import CRPTerror
from session import SessionLocal
from config import settings
from sqlalchemy.orm import Session
from conflog import log

import pandas as pd

db: Session = SessionLocal()



def show_data():
    """
    Извлекает отдельные элементы их кривого .CSV файла.
    """
    df = pd.read_csv("target/120_upd_error.csv")
    print(df)
    print(df[df.columns[0]])
    print(df[df.columns[0]][0].split(' ')[-1])
    print(" ".join(df[df.columns[0]][1].split(' ')[-3:]))
    print(df[df.columns[0]][5])
    print(df[df.columns[-1]][5])

def collect_data_to_db():
    """
    При запуске происходит чтение .CSV файла и формирование записи в БД.
    Поскольку в файле одна запись, запускать однократно.
    """
    df = pd.read_csv("target/120_upd_error.csv")
    item = CRPTerror()
    item.report_date = df[df.columns[0]][0].split(' ')[-1]
    item.report_period = " ".join(df[df.columns[0]][1].split(' ')[-3:])
    item.inn = df[df.columns[0]][5]
    item.doc = df[df.columns[-1]][5]
    # print(item)
    db.add(item)
    db.commit()


if __name__ == "__main__":
    # log.info(f"{settings.DB_NAME=}")
    # show_data()
    # collect_data_to_db()
    item = db.query(CRPTerror).first()
    print(f"{item.inn=}")
    assert item.inn.isnumeric()
