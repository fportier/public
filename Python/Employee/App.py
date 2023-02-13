
from Employee import  Employee
from HourlyEmployee import  HourlyEmployee

def main():
    emp1 = HourlyEmployee("Joe",100,"Manager",12.34)
    print(emp1)
    emp1.setWage(15.89)
    print(emp1)

    
main()