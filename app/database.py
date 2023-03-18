from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# "postgresql://<username>:<password>@localhost/<database_name>"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Iah%40#123123@localhost/books"



engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

