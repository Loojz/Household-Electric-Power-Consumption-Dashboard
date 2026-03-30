import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def get_engine():
    """Return SQLAlchemy engine using .env credentials."""
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    user = os.getenv("DB_USER", "luis")
    password = os.getenv("DB_PASSWORD", "")
    dbname = os.getenv("DB_NAME", "power_consumption")
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")


# Singleton-Engine für die gesamte App
engine = get_engine()
