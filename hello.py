class Test:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_bonus(self):
        bonus = self.salary * 0.1
        return bonus


t = Test("Ashutosh", 24, 100000)
print(t.get_bonus())
