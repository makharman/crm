import json
from user import User
import os

class SimpleProject:
    def __init__(self, json_file="data.json",data_directory="data"):
        self.json_file = json_file
        self.data_directory = data_directory
        self.users = self.load_data()

    def load_data(self):
        data_file_path = os.path.join(self.data_directory, self.json_file)
        with open(data_file_path, "r") as f:
            data = json.load(f)
            users_data = data.get("users", [])
            users = [User(user["id"], user["name"], user["age"]) for user in users_data]
            return users

    def display_users(self):
        print("\nUsers:")
        for user in self.users:
            user.display_info()

    def add_user(self, user_id, name, age):
        new_user = User(user_id, name, age)
        self.users.append(new_user)
        self.save_data()

    def save_data(self):
        data_file_path = os.path.join(self.data_directory, self.json_file)
        data = {"users": [{"id": user.id, "name": user.name, "age": user.age} for user in self.users]}
        with open(data_file_path, "w") as f:
            json.dump(data, f, indent=2)

    def run(self):
        print("1. All Users\n2. Add User\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.display_users()
        elif choice == "2":
            user_id = int(input("Enter User ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            self.add_user(user_id, name, age)
        else:
            print("Please try again.")

SimpleProject().run()

