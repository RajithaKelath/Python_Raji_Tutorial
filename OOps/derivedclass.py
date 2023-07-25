"""
create different payroll depend on employee position
#Hierarchial Inheritance - Single base class "Employee" is derived by multiple child class
"""

from baseclass import Employee

class SalaryEmployee(Employee):
    """
    Create salary struture for Salary based employees
    """

    #Initialize Instance attribute
    def __init__(self,name,id,weekly_salary):
        super().__init__(name,id)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    """
    Salary struture for Hourly based employee
    """
    def __init__(self,name,id,hourly_salary,hours):
        super().__init__(name,id)
        self.hourly_salary = hourly_salary
        self.hours = hours

    def calculate_payroll(self):
        return self.hourly_salary * self.hours
    

class CommissionEmployee(SalaryEmployee):
    """
    Salary struture for Commission based employee
    """
    #Multiline inheritance
    def __init__(self,name,id,weekly_salary,commission):
        super().__init__(name,id,weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


    

        