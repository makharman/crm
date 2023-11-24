class User:
    def __init__(self, user_id, name, age):
        self.id = user_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"User ID: {self.id}, Name: {self.name}, Age: {self.age}")



