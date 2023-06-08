# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import datetime
import time


class Test:

    @classmethod
    def setup_class(cls):
        start = datetime.datetime.now()
        print('Начало выполнения класса:', start)

    @classmethod
    def teardown_class(cls):
        end = datetime.datetime.now()
        print('Окончание выполнения класса:', end)

    def test_1(self, start_time):
        time.sleep(1)

    def test_2(self):
        time.sleep(2)

