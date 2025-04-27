def name ():
  firstName = input("Primer Nombre ")
  secondName= input("Segundo Nombre ")
  thirdName = input("Tercer Nombre ")
  
  fullName = firstName.capitalize() + " " + secondName.capitalize() + " " + thirdName.capitalize()
  return fullName

completN=name()
print(completN)
