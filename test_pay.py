import unittest
import emp

class test_emp(unittest.TestCase):

    

    def test_get_email(self):
        
        e1 = emp.Employee('Mike', 'Tyson', 100)
        e2 = emp.Employee('John', 'Snow', 200)
        
        self.assertEqual(e1.get_email, 'MikeTyson@mailll.ru')
        self.assertEqual(e2.get_email, 'JohnSnow@mailll.ru')

        e1.first = 'Nick'
        e2.first = 'Anthony'
        
        self.assertEqual(e1.get_email, 'NickTyson@mailll.ru')
        self.assertEqual(e2.get_email, 'AnthonySnow@mailll.ru')

    def test_full_name(self):

        e1 = emp.Employee('Mike', 'Tyson', 100)
        e2 = emp.Employee('John', 'Snow', 200)

        self.assertEqual(e1.full_name, 'Mike Tyson')
        self.assertEqual(e2.full_name, 'John Snow')

        e1.first = 'Nick'
        e2.first = 'Anthony'

        self.assertEqual(e1.full_name, 'Nick Tyson')
        self.assertEqual(e2.full_name, 'Anthony Snow')

    def test_pay_raise(self):

        e1 = emp.Employee('Mike', 'Tyson', 100)
        e2 = emp.Employee('John', 'Snow', 200)

        e1.pay_raise()
        e2.pay_raise()

        self.assertEqual(e1.pay, 105)
        self.assertEqual(e2.pay, 210)

if __name__ == '__main__':
    unittest.main()