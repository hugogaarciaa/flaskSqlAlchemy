import os
class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')