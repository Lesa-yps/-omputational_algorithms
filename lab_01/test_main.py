import mock
from main import *

def test_read_int():
    with mock.patch.object(__builtins__, 'input', lambda: '4'):
        assert read_int("Введите число: ") == 4
