import secrets
from fastapi.responses import JSONResponse
from fastapi_mail import MessageSchema, FastMail, ConnectionConfig
from config.config import Config

def generate_verification_token():
    return secrets.token_urlsafe(32)

async def send_verification_email(email: str, verification_token: str):
    subject = "Email Verification"
    verification_link = f"{Config.BASE_URL + Config.BASE_API}/auth/verify?token={verification_token}"
    body = f"Click <a href={verification_link}>{verification_link}</a> to verify your email."
    
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )

    conf = ConnectionConfig(
        MAIL_USERNAME = Config.MAIL_USERNAME,
        MAIL_PASSWORD = Config.MAIL_PASSWORD,
        MAIL_FROM = Config.MAIL_FROM,
        MAIL_PORT = Config.MAIL_PORT,
        MAIL_SERVER = Config.MAIL_SERVER,
        MAIL_STARTTLS = Config.MAIL_STARTTLS,
        MAIL_SSL_TLS = Config.MAIL_SSL_TLS,
        USE_CREDENTIALS = Config.USE_CREDENTIALS,
        VALIDATE_CERTS = Config.VALIDATE_CERTS
    )

    fm = FastMail(conf)
    await fm.send_message(message)