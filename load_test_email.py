import os
import time
from os.path import join, dirname

import jwt

from dotenv import load_dotenv
from locust import HttpUser, task

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class SendEmail(HttpUser):
    """
    Sends requests to POST v2/notifications/email
    """

    def on_start(self) -> None:
        self.api_key = os.environ.get("API_KEY")
        self.email_template_id = os.environ.get("EMAIL_TEMPLATE_ID")
        self.service_id = os.environ.get("SERVICE_ID")
