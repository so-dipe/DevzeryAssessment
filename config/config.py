import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST =  os.getenv("DB_HOST")
    DB_USER =  os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_USER")
    DB_PORT = os.getenv("DB_PORT")

    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    BASE_URL = os.getenv("BASE_URL")
    BASE_API = os.getenv("BASE_API")

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_STARTTLS = os.getenv("MAIL_TLS") if os.getenv("MAIL_TLS") else True
    MAIL_SSL_TLS = os.getenv("MAIL_SSL") if os.getenv("MAIL_SSL") else False
    USE_CREDENTIALS = os.getenv("USE_CREDENTIALS") if os.getenv("USE_CREDENTIALS") else True
    VALIDATE_CERTS = os.getenv("VALIDATE_CERTS") if os.getenv("VALIDATE_CERTS") else False

    SECRET_KEY = os.getenv("SECRET_KEY")