import Interface as inf
import derivedclass as dc

if __name__ == '__main__':
    salary_employee = dc.SalaryEmployee('John Smith', 1, 1500)
    hourly_employee = dc.HourlyEmployee('Jane Doe', 2, 40, 15)
    commission_employee = dc.CommissionEmployee('Kevin Bacon', 3, 1000, 250)
    payroll_system = inf.IPayrollPrint()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee
    ])