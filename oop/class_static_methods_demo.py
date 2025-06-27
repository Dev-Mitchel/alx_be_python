class Calculator:
    # class attribute
    calculator_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
     
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculator type : {cls.calculator_type}")
        return a * b
    
       
        
  
        