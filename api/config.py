import os
import secrets
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get("ONCE_SECRET_KEY") or "".join(secrets.token_hex(16))
    SQUIRREL_MONGO_URI = os.environ.get("SQUIRREL_MONGO_URI")
