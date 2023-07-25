"""
Payroll print for employees
IPayrollPrint Implement the calculate.payroll() method for collection of employee
"""
class IPayrollPrint:

    #Print payroll for employees
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        print("=" * 20)
        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"-check amount: {employee.calculate_payroll()}")
            print('')

