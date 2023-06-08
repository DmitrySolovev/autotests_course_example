import pytest
import datetime


@pytest.fixture
def start_time():
    print('Начало теста:', datetime.datetime.now())


