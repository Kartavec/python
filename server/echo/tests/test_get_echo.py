import pytest
from echo.controllers import get_echo
from datetime import datetime

@pytest.fixture
def action_fixture():
    print('connect to db')
    return 'echo'

@pytest.fixture
def time_fixture():
    return datetime.now().timestamp()

@pytest.fixture
def data_fixture():
    return 'some data'

@pytest.fixture
def request_fixture(action_fixture, time_fixture, data_fixture):
    return  {
        'action':action_fixture,
        'time': time_fixture,
        'data': data_fixture
    }

@pytest.fixture
def response_fixture(action_fixture, time_fixture,data_fixture):
    return {
        'action': action_fixture,
        'time': time_fixture,
        'data': data_fixture,
        'user': None,
        'code': 200
    }

def test_get_echo(request_fixture, response_fixture):
    response = get_echo(request_fixture)

    assert response_fixture.get('code') == response.get('code')

