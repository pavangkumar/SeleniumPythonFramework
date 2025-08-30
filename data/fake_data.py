# data/fake_data.py
from faker import Faker

fake = Faker()

def valid_billing_address_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address_1": fake.street_address(),
        "city": fake.city(),
        "postcode": fake.postcode(),
        "phone": "7337089325",
        "email": fake.safe_email()
    }

def invalid_billing_data():
    return [
        {"field": "first_name", "value": "", "error_key": "first_name_error"},
        {"field": "last_name", "value": "", "error_key": "last_name_error"},
        {"field": "address_1", "value": "", "error_key": "address_1_error"},
        {"field": "city", "value": "", "error_key": "city_error"},
        {"field": "postcode", "value": "12", "error_key": "postcode_error"},
        {"field": "phone", "value": "", "error_key": "phone_error"},
        {"field": "phone", "value": "abc123", "error_key": "phone_error"},
        {"field": "email", "value": "not-an-email", "error_key": "email_error"}
    ]
