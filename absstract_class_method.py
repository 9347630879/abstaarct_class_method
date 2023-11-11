from abc import ABC, abstractmethod


class Employee(ABC):
    fName: str = " "
    lName: str = " "
    pay: float = 2545897215154000

    @abstractmethod
    def sal(self):
        pass

    @classmethod
    def setfullName(cls, fname: str, lname: str):
        cls.fName = fname
        cls.lName = lname

    @classmethod
    def getfullName(cls):
        return f'{cls.fName} {cls.lName}'


class permanentEmployee(Employee):
    def sal(self):
        return 12 * self.pay


emp = permanentEmployee()
emp.setfullName("Sai", "Sundhar")
n = emp.getfullName()
s = emp.sal()
print(n)
print(s)


class employee(ABC):
    fname:str = " "
    lname : str = " "
    pay:float = 52
    @abstractmethod
    def sal(self):
        pass
    @classmethod
    def setfullname(cls,fname:str,lname:str):
        cls.fname = fname
        cls.lname = lname
    @classmethod
    def getfullname(cls):
        return f'{cls.fname} {cls.lname}'
class secure(employee):
    def sal(self):
        return 12*self.pay
emp = secure()
emp.setfullname("gokavaram","dhanunjai")
name = emp.getfullname()
d = emp.sal()
print(name)
print(d)
