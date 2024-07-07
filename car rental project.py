class Car:
    def __init__(self, name, year, number):
        self.name = name
        self.year = year
        self.number = number
        self.is_rented = False
    
    def display(self):
        print("Car name:", self.name)
        print("Car year:", self.year)
        print("Car number:", self.number)
        print("Rental status:", "Rented" if self.is_rented else "Available")
    
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"{self.name} has been rented.")
        else:
            print(f"Sorry, {self.name} is already rented.")
    
    def return_car(self):
        if self.is_rented:
            self.is_rented = False
            print(f"{self.name} has been returned.")
        else:
            print(f"{self.name} was not rented out.")

class Registration:
    def __init__(self, rental_system):
        self.rental_system = rental_system
    
    def register_car(self):
        name = input("Enter car name: ")
        year = int(input("Enter car year: "))
        number = int(input("Enter car number: "))
        
        new_car = Car(name, year, number)
        self.rental_system.cars.append(new_car)
        print(f"{name} has been successfully registered.")
        
class RentalSystem:
    def __init__(self):
        self.cars = []
        self.create_initial_cars()
    
    def create_initial_cars(self):
        car1 = Car("Verna", 2020, 1)
        car2 = Car("Ferrari", 2021, 2)
        car3 = Car("Lemborgini", 2022, 3)
        self.cars.extend([car1, car2, car3])
    
    def display_available_cars(self):
        print("Available Cars:")
        for car in self.cars:
            if not car.is_rented:
                car.display()
                print()  
    
    def rent_car(self, car_name):
        for car in self.cars:
            if car.name.lower() == car_name.lower():
                car.rent()
                return
        print(f"Sorry, {car_name} is not available for rent.")
    
    def return_car(self, car_name):
        for car in self.cars:
            if car.name.lower() == car_name.lower():
                car.return_car()
                return
        print(f"Cannot return {car_name}: car not found.")

def main():
    rental_system = RentalSystem()
    registration = Registration(rental_system)
    
    while True:
        print("\nMenu:")
        print("1. Display available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Register a new car")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            rental_system.display_available_cars()
        elif choice == "2":
            car_name = input("Enter the name of the car you want to rent: ")
            rental_system.rent_car(car_name)
        elif choice == "3":
            car_name = input("Enter the name of the car you want to return: ")
            rental_system.return_car(car_name)
        elif choice == "4":
            registration.register_car()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()




