#inherit class
class Parents:
 name = "Father"
 def DoIt(self):
  age = 40
  print(age)
class daughter(Parents):
 pass
 
m = daughter()
m.DoIt()
print(m.name)