import pytest

class Test_demo:

    def test_one(self):
        a=1
        b=4
        assert a>b, "a is not greater than b"

    def test_two(self):
        a=2
        b=4
        assert a<b, "a is not less than b"

    def test_three(self):
        a=4
        b=4
        assert a == b, "a is not equal than b"

    def test_four(self):
        a=3
        b=4
        assert a*b > 10, "a*b is not greater than 10"

    def test_five(self):
        a=5
        b=4
        assert a-b == 1, "a-b is not equla to 1"

    def test_six(self):
        a=11
        b=4
        assert a>b, "a is not greater than b"

    def test_seven(self):
        a = 6
        b = 41
        assert a < b, "a is not less than b"

    def test_eigth(self):
        a = 4
        b = 4
        assert a == b, "a is not equal than b"

    def test_nine(self):
        a = 6
        b = 4
        assert a * b > 10, "a*b is not greater than 10"

    def test_ten(self):
        a = 5
        b = 4
        assert a - b == 1, "a-b is not equla to 1"



