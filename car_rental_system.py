import json
import os

class CarRentalSystem:
    def __init__(self):
        self.cars_file = "cars.json"
        self.load_data()

        # Basic login data (username: password)
        self.users = {
            "admin": "admin123",
            "john": "pass123",
            "mary": "qwerty"
        }

        self.current_user = None

    def load_data(self):
        if os.path.exists(self.cars_file):
            with open(self.cars_file, "r") as file:
                self.cars = json.load(file)
        else:
            self.cars = {
                "KCN 123X": {"model": "Toyota Vitz", "available": True},
                "KDA 456Y": {"model": "Mazda Demio", "available": True},
                "KDE 789Z": {"model": "Honda Fit", "available": True}
            }

    def save_data(self):
        with open(self.cars_file, "w") as file:
            json.dump(self.cars, file, indent=4)

    def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")

        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"✅ Welcome, {username}!")
            return True
        else:
            print("❌ Login failed. Invalid credentials.")
            return False

    def display_available_cars(self):
        print("\nAvailable Cars:")
        for plate, details in self.cars.items():
            if details["available"]:
                print(f"  {plate} - {details['model']}")

    def display_all_cars(self):
        print("\nAll Cars (Admin View):")
        for plate, details in self.cars.items():
            status = "Available" if details["available"] else "Booked"
            print(f"  {plate} - {details['model']} ({status})")

    def book_car(self):
        plate = input("\nEnter the car plate number to book: ").upper()
        if plate in self.cars and self.cars[plate]["available"]:
            try:
                days = int(input("Enter number of rental days: "))
                if days <= 0:
                    print("❌ Invalid number of days.")
                    return
            except ValueError:
                print("❌ Please enter a valid number.")
                return

            cost_per_day = 3000
            total_cost = days * cost_per_day
            self.cars[plate]["available"] = False
            self.save_data()

            print(f"\n✅ Booking Confirmed for {self.cars[plate]['model']} ({plate})")
            print("Generating receipt...")

            receipt = f"""
========= CAR RENTAL RECEIPT =========
Customer: {self.current_user}
Car: {self.cars[plate]['model']}
Plate Number: {plate}
Rental Duration: {days} day(s)
Rate: Ksh {cost_per_day}/day
--------------------------------------
Total: Ksh {total_cost}
======================================
"""
            print(receipt)

            with open(f"receipt_{plate}.txt", "w") as file:
                file.write(receipt)

        else:
            print("❌ Car is not available or invalid plate number.")

    def return_car(self):
        plate = input("\nEnter the car plate number to return: ").upper()
        if plate in self.cars and not self.cars[plate]["available"]:
            self.cars[plate]["available"] = True
            self.save_data()
            print(f"✅ Car {self.cars[plate]['model']} ({plate}) returned.")
        else:
            print("❌ Invalid return. Check the plate number or status.")

    def run(self):
        if not self.login():
            return

        while True:
            print("\n--- Car Rental System ---")
            print("1. View Available Cars")
            print("2. Book a Car")
            print("3. Return a Car")
            if self.current_user == "admin":
                print("4. View All Cars (Admin)")
                print("5. Exit")
            else:
                print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.display_available_cars()
            elif choice == '2':
                self.book_car()
            elif choice == '3':
                self.return_car()
            elif choice == '4' and self.current_user == "admin":
                self.display_all_cars()
            elif (choice == '4' and self.current_user != "admin") or (choice == '5' and self.current_user == "admin"):
                print("👋 Logging out. See you!")
                break
            else:
                print("⚠️ Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    system = CarRentalSystem()
    system.run()
