class AgeException(Exception):
    def __init__(self, age, message="Age must be between 18 to 100"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def message_true(self):
        print(f"Age is set to {self.age}")

    def message_false(self):
        print(f"Invalid Age: {self.age}. {self.message}")


age = int(input("Enter the age: "))
if age < 18 or age > 100:  # Corrected logical condition
    e = AgeException(age)
    e.message_false()
else:
    e = AgeException(age)
    e.message_true()