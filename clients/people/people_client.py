from time import time
from clients.base_client import BaseClient
from config import people_api_base_url as base_url
from utils.request import *


class PeopleClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = base_url

    def create_new_unique_user(self, body=None):
        if not body:
            unique_lastname = f'User_{time()}'
            payload = {
                'fname': 'New',
                'lname': unique_lastname
            }
        else:
            unique_lastname = body['lname']
            payload = body

        print(f'payload: {payload}')
        print(f'lastname: {unique_lastname}')
        status_code, peoples, response_headers = post_resource(url=self.base_url, payload=payload, headers=self.headers)
        return unique_lastname, status_code, peoples, response_headers

    def read_all_persons(self):
        return get_resource(self.base_url)

    def delete_person(self, person_id):
        url = f'{self.base_url}/{person_id}'
        return delete_resource(url)

    def update_person(self, person_id):
        url = f'{self.base_url}/{person_id}'
        new_last_name = 'some_random_name'
        payload = {
            'lname': new_last_name
        }
        status_code, peoples, response_headers = update_resource(url, payload, self.headers)
        return new_last_name, status_code, peoples, response_headers
