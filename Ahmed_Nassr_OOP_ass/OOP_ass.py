class Person:
    def __init__(self, name, money=0, mood="neutral", health_rate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= 10 * items


class Car:
    def __init__(self, name, fuel_rate=100, velocity=0):
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

    def run(self, velocity, distance):
        if velocity > 200 or velocity < 0:
            raise ValueError("Velocity must be between 0 and 200.")
        self.velocity = velocity

        fuel_consumed = (distance / 10) * 10  # 10% fuel consumed every 10 km
        self.fuel_rate -= fuel_consumed

        if self.fuel_rate <= 0:
            self.stop(distance)
        else:
            self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped. Remaining distance: {remaining_distance} km.")
        else:
            print("Car arrived at the destination.")


class Employee(Person):
    def __init__(self, name, id, car, email, salary, distance_to_work):
        super().__init__(name)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, gas_amount=100):
        self.car.fuel_rate += gas_amount
        if self.car.fuel_rate > 100:
            self.car.fuel_rate = 100

    def send_mail(self, to, subject, msg):
        print(f"Email sent to {to} with subject '{subject}': {msg}")


class Office:
    employees_num = 0  

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employees_num -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            target_hour = 9  
            distance = emp.distance_to_work
            velocity = emp.car.velocity
            is_late = Office.calculate_lateness(target_hour, move_hour, distance, velocity)
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        if velocity == 0:
            return True  
        time_to_office = distance / velocity
        arrival_hour = move_hour + time_to_office
        return arrival_hour > target_hour


# Use Case
if __name__ == "__main__":
    samy_car = Car(name="Fiat 128")

    samy = Employee(name="Samy", id=1, car=samy_car, email="samy@iti.com", salary=5000, distance_to_work=20)

    iti_office = Office(name="ITI Smart Village")

    iti_office.hire(samy)

    # Simulate Samy's day
    samy.sleep(7)  # Samy sleeps for 7 hours
    samy.eat(3)  # Samy eats 3 meals
    samy.buy(2)  # Samy buys 2 items

    samy.drive(distance=20, velocity=60)  # Drives 20 km at 60 km/h

    iti_office.check_lateness(emp_id=1, move_hour=8)  # Samy left at 8 AM

    print(f"{samy.name}'s mood: {samy.mood}")
    print(f"{samy.name}'s health rate: {samy.health_rate}%")
    print(f"{samy.name}'s salary: {samy.salary} L.E")
    print(f"{samy.name}'s car fuel rate: {samy.car.fuel_rate}%")