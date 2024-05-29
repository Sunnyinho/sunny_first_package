class Calculator:
    def __init__(self,  a, b):
        self.a = a
        self.b = b
        self.addition()
        self.subtraction()
        self.multiplication()
        self.division()

    def addition(self):
        return f"The addition value is: {self.a + self.b}"

    def subtraction(self):
        return f"The subtraction value is: {self.a - self.b}"

    def multiplication(self):
        return f"The multiplication value is: {self.a * self.b}"

    def division(self):
        return f"The division value is: {self.a / self.b}"
    
    def get_celing_value(self):
        return f"The celing value is: {self.a // self.b}"
