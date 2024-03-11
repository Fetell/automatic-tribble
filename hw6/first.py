"""
Документация API: https://restful-booker.herokuapp.com/apidoc/index.html

1. Воспроизвести все методы, рассмотренные на лекции
2. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
3. Проверить, что изменения применились

Также вы можете тренироваться на следующих сайтах:
https://jsonplaceholder.typicode.com
https://playground.learnqa.ru/api/map
"""


import pytest
import requests
# import fixtures
import settings


@pytest.fixture(scope="module")
def auth_token():
    payload = {
        "username": settings.LOGIN,
        "password": settings.PASSWORD}
    request = requests.post(settings.AUTH_URL, json=payload)
    yield {"Cookie": f"token={request.json()["token"]}"}


@pytest.fixture(scope="session")
def booking_id():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    request = requests.post(settings.BOOKING_URL, json=payload)
    yield request.json()['bookingid']



@pytest.mark.smoke
def test_code_ok():
    request = requests.get(settings.BOOKING_URL)
    print(request)
    assert request.status_code == 200


@pytest.mark.skip
def test_get_first_booking():
    request = requests.get(f'{settings.BOOKING_URL}/1')
    response_data = request.json()
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    ]
    assert request.status_code == 200
    print(response_data)
    print(len(response_data.keys()))
    assert len(response_data.keys()) == len(expected_keys)
    for key in expected_keys:
        assert key in response_data.keys()


@pytest.mark.regression
@pytest.mark.xfail(reason="Wrong status code")
def test_get_booking_by_id(booking_id):
    request = requests.get(f'{settings.BOOKING_URL}/{booking_id}')
    assert request.status_code == 200
    data = request.json()
    print(data)
    assert data['firstname'] == "James"


def test_update_booking(auth_token, booking_id):
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Lunch"
    }
    request = requests.post(f'{settings.BOOKING_URL}/{booking_id}', payload, auth_token)
    assert request.status_code == 200
    request_2 = requests.get(f'{settings.BOOKING_URL}/{booking_id}')
    print(request_2)
    assert request_2.json()["additionalneeds"] == "Lunch"


def test_delete_booking(auth_token, booking_id):
    request = requests.delete(f'{settings.BOOKING_URL}/{booking_id}', headers=auth_token)
    assert request.status_code == 201
    request_get = requests.get(f'{settings.BOOKING_URL}/{booking_id}')
    assert request_get.status_code == 404

