import random
import pytest
from utils.file_reader import read_file


@pytest.fixture
def create_data():
    payload = read_file('create_person_request_template.json')

    random_no = random.randint(0, 1000)
    last_name = f'User_{random_no}'

    payload['lname'] = last_name
    return payload
