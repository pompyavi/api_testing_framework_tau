from assertpy import assert_that


def assert_people_have_person_with_first_name(response, first_name):
    assert_that(response).extracting('fname').is_not_empty().contains(first_name)


def assert_person_is_present(new_user):
    assert_that(new_user).is_not_empty()


def assert_person_lastname_is_updated(updated_person, new_lastname):
    assert_that(updated_person['lname']).is_equal_to(new_lastname)
