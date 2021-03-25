import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"

POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "postgres"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", ""),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", ""),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5432),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "postgres"),
}

DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

SQLALCHEMY_POOL_SIZE = 2
SQLALCHEMY_MAX_OVERFLOW = 0
