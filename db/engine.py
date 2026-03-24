from sqlalchemy import create_engine
from db.models import Base

sqlite_db = "sqlite:///stalcraft.db"

engine = create_engine(url=sqlite_db)

Base.metadata.create_all(bind=engine)