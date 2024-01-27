import pytest
import requests
from assertpy import soft_assertions
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from clients.people.people_client import PeopleClient
from tests.assertions.people_assertions import *
from tests.helpers.people_helper import get_user, search_nodes_using_json_path
from utils.file_reader import read_file

client = PeopleClient()


def test_get_all_people_has_bunny():
    status_code, peoples, _ = client.read_all_persons()
    assert_that(status_code).is_equal_to(requests.codes.ok)
    assert_people_have_person_with_first_name(peoples, first_name='Bunny')
    schema = read_file('schema.json')
    with soft_assertions():
        for people in peoples:
            try:
                validate(instance=people, schema=schema)
            except ValidationError as e:
                pytest.fail(f"Schema validation failed: {e.message}")


def test_new_person_can_be_added():
    lastname, status_code, _, _ = client.create_new_unique_user()
    assert_that(status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    _, peoples, _ = client.read_all_persons()
    new_user = get_user(lastname, peoples)
    assert_person_is_present(new_user)


def test_user_can_be_deleted():
    lastname, _, _, _ = client.create_new_unique_user()
    _, peoples, _ = client.read_all_persons()
    user_to_be_deleted = get_user(lastname, peoples)['person_id']
    status_code, _, _ = client.delete_person(user_to_be_deleted)
    assert_that(status_code).is_equal_to(requests.codes.all_okay)


def test_user_lastname_can_be_updated():
    lastname, _, _, _ = client.create_new_unique_user()
    _, peoples, _ = client.read_all_persons()
    user_to_be_updated = get_user(lastname, peoples)['person_id']
    new_lastname, status_code, updated_person, _ = client.update_person(user_to_be_updated)
    assert_that(status_code).is_equal_to(requests.codes.all_okay)
    assert_person_lastname_is_updated(updated_person, new_lastname)


def test_person_can_be_added_with_a_json_template(create_data):
    client.create_new_unique_user(create_data)
    status_code, peoples, _ = client.read_all_persons()

    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
