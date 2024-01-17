

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def get_email(self):
        return f'{self.first}{self.last}@mailll.ru'
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def pay_raise(self):
        self.pay *= self.raise_amount

