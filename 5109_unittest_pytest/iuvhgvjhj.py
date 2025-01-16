import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(10, 'a1')


def test_wrong_type2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a22', 'a1')


def test_wrong_type3():
    with pytest.raises(TypeError):
        is_under_queen_attack('a1', 10)


def test_wrong_type2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a1', 'a13')


def test_reverse3():
    assert is_under_queen_attack('a1', 'b2')


def test_reverse4():
    assert is_under_quenn_attack('a2', 'b2')


def test_reverse5():
    assert is_under_queen_attack('a1', 'h1')


if __name__ == '__main__':
    pytest.main()
