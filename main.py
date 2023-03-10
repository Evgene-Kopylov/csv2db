from session import SessionLocal
from config import settings
from sqlalchemy.orm import Session
from conflog import log


db: Session = SessionLocal()

if __name__ == "__main__":
    print("hello world")
