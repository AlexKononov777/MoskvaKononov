from reverse import reverse
import unittest

def reverse(s):
    if type(s) != str:
        raise TypeError(f'Необходим str, а не {type(s)}')
    return s[::-1]
class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_1(self):
        self.assertEqual(reverse('f'), 'f')

    def test_slova(self):
        self.assertEqual(reverse('fgg'), 'ggf')

    def test_spiska(self):
        with self.assertRaises(TypeError):
            reverse(['d', 'ds'])



if __name__ == '__main__':
    unittest.main()