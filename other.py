class employee:
    def __init__(self,name,job_title,salary):
        self.name = name
        self.jobtitle = job_title
        self.salary = salary
    def increase_salary(self):
        self.salary = self.salary + 10000

class manager(employee):
    def __init__(self,name,job_title,salary):
        super().__init__(name,job_title,salary) #  This super reffers to the parent of the child class
        self.employees_managed = []


    def increase_salary(self):
    #   [self.salary = self.salary + 100000] super function can be used to increase the managers salary by twice of the employees one
        super().increase_salary()
        super().increase_salary()
