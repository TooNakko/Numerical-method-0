class Dec(float):
   def __init__(self, n: float, precision: int =1):
      self.num = n
      self.p = precision
      super().__init__()

   def __str__(self) -> str:
      return f"{self.num:.{self.p+1}}"
   


a = Dec(2.128936745187634)
b = Dec(12)
print(a/b)
print(2.1/12)