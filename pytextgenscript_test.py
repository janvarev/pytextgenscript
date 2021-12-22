import unittest
import pytextgenscript as ptgs


class TestPyTextGen(unittest.TestCase):

    def test_1(self):
        ''' Тестирует корректность обработки вложенных структур'''
        self.assertEqual(ptgs.run_s('("a" "b" "c")'), "abc")

    def test_2(self):
        ''' Тестирует корректность обработки вложенных структур'''
        self.assertEqual(ptgs.run_s('("a" ("b" "c") "d")'), "abcd")

    def test_3(self):
        ''' Тестирует корректность обработки метода рандомной генерации'''
        res = ptgs.run_s('("a" (#r "b" "c") "d")')
        self.assertTrue((res == "abd") or (res == "acd"))

    def test_4(self):
        ''' Тестирует корректность обработки диапазона выбора метода рандомной генерации'''
        self.assertEqual(ptgs.run_s('( "a" (#r "b") "d")'), "abd")

    def test_5(self):
        ''' Тестирует корректность обработки объединения метода рандомной генерации
        и вложенных структур'''
        res = ptgs.run_s('("a" ("p" (#r "b" "c")) "d")')
        self.assertTrue((res == "apbd") or (res == "apcd"))

    def test_6(self):
        ''' Тестирует корректность обработки метода инициализации переменных'''
        self.assertEqual(ptgs.run_s('((#varSet "x" "b") ("a" @x))'), "ab")

    def test_7(self):
        ''' Тестирует корректность обработки метода инициализации переменных и
        условного оператора'''
        self.assertEqual(ptgs.run_s('((#varSet "x" "b") ("a" (#ifVarEq "x" "b" "tr" "fal")))'), "atr")

    def test_8(self):
        ''' Тестирует корректность инициализации и вызова переменных'''
        self.assertEqual(ptgs.run_s('("a" (#varSet "x" "b") @x (#varSet "y" "d") @y)'), "abd")

    def test_9(self):
        ''' Тестирует корректность обработки метода инициализации переменных и
         условного оператора'''
        self.assertEqual(ptgs.run_s('("a" (#varSet "x" "b") (#ifVarEq "x" "c" "tr" "fal"))'), "afal")

    def test_10(self):
        ''' Тестирует переменные как параметр'''
        self.assertEqual(ptgs.run_s('(("a" @x))',{'x':"b"}), "ab")

    def test_nl(self):
        ''' Тестирует new line'''
        self.assertEqual(ptgs.run_s('("a" #nl "c")'), "a\r\nc")

if __name__ == '__main__':
    unittest.main()