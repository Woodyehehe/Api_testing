from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert

#hw 14, task 2
def test_register():
    email = 'eve.holt@reqres.in'
    password = 'password12345'
    res = api.register(password)
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)
    assert res.headers['Content-Type'] == 'application/json'

# hw 14 task 3
def test_register_error():
    res = api.register_error()
    res_body = res.json()

    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res_body)
    assert res.headers['Content-Type'] == 'application/json'
    example = {
        "error": "Missing password"
    }

    assert example == res_body
