import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("ONCE_SECRET_KEY") or "".join(secrets.token_hex(16))