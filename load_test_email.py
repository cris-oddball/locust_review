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
        self.api_key = os.environ.get('API_KEY')
        self.email_address = os.environ.get('EMAIL_ADDRESS')
        self.email_template_id = os.environ.get('EMAIL_TEMPLATE_ID')
        self.service_id = os.environ.get('SERVICE_ID')

    def _get_jwt(self) -> str:
        header = {'typ': 'JWT', 'alg': 'HS256'}
        combo = {}
        currentTimestamp = int(time.time())
        data = {
            'iss': self.service_id,
            'iat': currentTimestamp,
            'exp': currentTimestamp + 30,
            'jti': 'jwt_nonce'
        }
        combo.update(data)
        combo.update(header)
        encoded_jwt = jwt.encode(combo, self.api_key, algorithm='HS256')
        return encoded_jwt

    @task
    def send(self):
        encoded_jwt = self._get_jwt()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {encoded_jwt}"
        }
        payload = {
            'template_id': self.email_template_id,
            'email_address': self.email_address
        }
        self.client.post(
            '/v2/notifications/email',
            json=payload,
            headers=headers
        )
