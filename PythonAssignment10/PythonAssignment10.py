class Car:
    def __init__(self, manufacturer, model, year = 2018, color = "black"):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model
        self. year = year

    def print(self):
        print(f"{self.manufacturer}, {self.model}, {self.year}, {self.color}")

My_Car = Car("Tesla", "Model Y", 2025)
My_Other_Car = Car("Mazda", "CX-5", color = "Red")
My_Car.print()
My_Other_Car.print()



class Solid:
    def __init__(self):
        pass

    def SurfaceArea(self):
        pass

    def volume(self):
        pass

class Cube(Solid):
    def __init__(self, SideLength):
        self.SideLength = SideLength

    def SurfaceArea(self):
        SurfaceArea = (self.SideLength ** 2) * 6
        print(SurfaceArea)

    def Volume(self):
        Volume = self.SideLength ** 3
        print(Volume)


class Sphere(Solid):
    def __init__(self, Radius):
        self.Radius = Radius

    def SurfaceArea(self):
        SurfaceArea = self.Radius * 3.14 * 2
        print(SurfaceArea)

    def Volume(self):
        Volume = (self.Radius ** 2) * 3.14
        print(Volume)



Rubiks_Cube = Cube(3)
Eight_Ball = Sphere(4)
Rubiks_Cube.SurfaceArea()
Rubiks_Cube.Volume()
Eight_Ball.SurfaceArea()
Eight_Ball.Volume()





class Employee:
    def __init__(self):
        pass

    def describe(self):
        print("I am an Employee.")


class Manager(Employee):
    def describe(self):
        super().describe()
        print("I manage a team.")


Manager = Manager()
Manager.describe()




class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display_account(self):
        print(f"{self.account_number}, {self.balance}, {self.interest_rate}")

    def add_interest(self):
        self.balance *= self.interest_rate



My_Savings = SavingsAccount(2, 248.32, 1.04)
My_Savings.display_account()
My_Savings.add_interest()
My_Savings.display_account()
My_Savings.add_interest()
My_Savings.display_account()
My_Savings.add_interest()
My_Savings.display_account()
My_Savings.add_interest()
My_Savings.display_account()
My_Savings.add_interest()
My_Savings.display_account()








