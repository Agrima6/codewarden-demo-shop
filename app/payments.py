import requests

from app.config import get_secret


def charge(amount_cents, token):
    resp = requests.post(
        "https://payments.example.com/v1/charges",
        auth=(get_secret("PAYMENT_API_KEY"), ""),
        data={"amount": amount_cents, "source": token},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()
