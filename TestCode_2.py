class Employee:
    def __init__(self, id = 10, name = "John"):
        self.id = id
        self.name = name
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
    # Creating a emp instance of Employee class  
  
emp = Employee() 
emp.display() 
  
# # Deleting the property of object 
del emp.id
del emp.name
# delattr(emp, 'id')
# # Deleting the object itself  
del emp