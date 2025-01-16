from reverse import reverse
import pytest

def test_reverse():
    assert reverse('123') == '321'

def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)

def test_reverse1():
    assert reverse('') == ''


def test_reverse2():
    assert reverse('lok kol') == 'lok kol'

def test_reverse3():
    assert reverse('a') == 'a'

def test_wrong_type2():
    with pytest.raises(TypeError):
        reverse(['42', 'k'])

if __name__ == '__main__':
    pytest.main()