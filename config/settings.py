import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("QA_USERNAME")
PASSWORD = os.getenv("QA_PASSWORD")

BASE_URL = "https://global.oliveyoung.com/"
LOGIN_URL = "https://global.oliveyoung.com/member/login"

DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 3