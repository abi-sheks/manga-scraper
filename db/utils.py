from db.models import database
from dotenv import load_dotenv
import os

def init_database():
    load_dotenv()
    database.init("manga", user='postgres',
                                 password=os.getenv("POSTGRES_PASSWORD"),
                                 host=os.getenv("POSTGRES_HOST"),
                                 port=os.getenv("POSTGRES_PORT"),
                                 )