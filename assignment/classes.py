class workers:
   def __init__(self, fname, lname, age, salary):
      self.fname = fname
      self.lname = lname
      self.age = age
      self.salary = salary


   def salary_decreament(self):
          self.salary -= self.salary * 0.08


   





class cars:
   def __init__(self, make, model):
      self.make = make
      self.model = model
      




import random

class randomnumbers:
   def __init__(self, minvalue, maxvalue):
       self.minvalue = minvalue
       self.maxvalue = maxvalue

       self.numbers = random.randint(self.minvalue, self.maxvalue)
       print(self.numbers)





