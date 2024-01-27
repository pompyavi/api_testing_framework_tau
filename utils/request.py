import requests


def get_response(response):
    status_code = response.status_code

    try:
        as_dict = response.json()
    except Exception:
        as_dict = {}

    headers = response.headers

    return status_code, as_dict, headers


def get_resource(url):
    response = requests.get(url)
    return get_response(response)


def post_resource(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)
    return get_response(response)


def update_resource(url, payload, headers):
    response = requests.put(url, json=payload, headers=headers)
    return get_response(response)


def delete_resource(url):
    response = requests.delete(url)
    return get_response(response)
