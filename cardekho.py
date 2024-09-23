import random
import string
import os

class Car:
    def __init__(self, name, year, number, photo_path=None):
        self.name = name
        self.year = year
        self.number = number
        self.is_rented = False
        self.photo_path = photo_path 

    def display(self):
        print("Car name:", self.name)
        print("Car year:", self.year)
        print("Car number:", self.number)
        print("Rental status:", "Rented" if self.is_rented else "Available")
        if self.photo_path:
            print("Photo path:", self.photo_path)

    def rent(self, mobile_number):
        if not self.is_rented:
            self.is_rented = True
            print(f"{self.name} has been rented.")
        else:
            print(f"Sorry, {self.name} is already rented.")

    def return_car(self, mobile_number):
        if self.is_rented:
            self.is_rented = False
            print(f"{self.name} has been returned.")
        else:
            print(f"{self.name} was not rented out.")

class Registration:
    def __init__(self, rental_system):
        self.rental_system = rental_system
        self.verified_mobile_numbers = set()

    def register_user(self):
        self.register_mobile()

    def register_mobile(self):
        mobile_number = input("Enter your mobile number for registration: ")
        if mobile_number in self.verified_mobile_numbers:
            print("Mobile number is already verified.")
            return
        
        verification_code = self.send_verification_sms(mobile_number)
        print(f"A verification code has been sent to {mobile_number}. Please check your messages.")

        user_code = input("Enter the verification code you received: ")
        if user_code == verification_code:
            self.verified_mobile_numbers.add(mobile_number)
            print("Mobile number verified successfully!")
        else:
            print("Verification failed. Please try again.")

    def send_verification_sms(self, mobile_number):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print(f"SMS sent to {mobile_number}: Your verification code is: {code}")
        return code

    def register_car(self):
        name = input("Enter car name: ")
        year = int(input("Enter car year: "))
        number = int(input("Enter car number: "))
        
        car_photo = input("Enter the path to the car photo: ")
        if not os.path.isfile(car_photo):
            print("Photo not found. Please check the path.")
            return
        
        new_car = Car(name, year, number, car_photo)
        self.rental_system.cars.append(new_car)
        print(f"{name} has been successfully registered.")

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.create_initial_cars()

    def create_initial_cars(self):
        car1 = Car("Verna", 2020, 1, "verna.jpg")
        car2 = Car("Ferrari", 2021, 2, "ferrari.jpg")
        car3 = Car("Lamborghini", 2022, 3, "lamborghini.jpg")
        self.cars.extend([car1, car2, car3])

    def display_available_cars(self):
        print("Available Cars:")
        for car in self.cars:
            if not car.is_rented:
                car.display()
                print()

    def rent_car(self, car_name, mobile_number):
        for car in self.cars:
            if car.name.lower() == car_name.lower():
                car.display() 
                confirm = input("Do you want to rent this car? (yes/no): ")
                if confirm.lower() == "yes":
                    car.rent(mobile_number)
                else:
                    print("Rental canceled.")
                return
        print(f"Sorry, {car_name} is not available for rent.")

    def return_car(self, car_name, mobile_number):
        for car in self.cars:
            if car.name.lower() == car_name.lower():
                car.return_car(mobile_number)
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
        print("5. Register a user")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            rental_system.display_available_cars()
        elif choice == "2":
            car_name = input("Enter the name of the car you want to rent: ")
            mobile_number = input("Enter your mobile number: ")
            rental_system.rent_car(car_name, mobile_number)
        elif choice == "3":
            car_name = input("Enter the name of the car you want to return: ")
            mobile_number = input("Enter your mobile number: ")
            rental_system.return_car(car_name, mobile_number)
        elif choice == "4":
            registration.register_car()
        elif choice == "5":
            registration.register_user()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
