import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "10"))
