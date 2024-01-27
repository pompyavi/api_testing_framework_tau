from jsonpath_ng import parse


def get_user(unique_lastname, response):
    return [people for people in response if people['lname'] == unique_lastname][0]


def search_nodes_using_json_path(peoples, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(peoples)]
