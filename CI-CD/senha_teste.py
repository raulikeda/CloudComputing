import unittest
import senha

class TesteData(unittest.TestCase):
    def test_should_return_true_when_senha_forte(self):
        self.assertTrue(senha.verifica_forca_senha('aA@13dsY'))
    def test_should_return_false_when_data_is_invalid(self):
        self.assertFalse(senha.verifica_forca_senha('1234'))
        self.assertFalse(senha.verifica_forca_senha('abcd1234'))
        self.assertFalse(senha.verifica_forca_senha('Abcd1234'))

if __name__ == '__main__':
    unittest.main()
