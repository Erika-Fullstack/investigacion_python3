
 # NAMING CONVENTIONS

"""1. Variable Naming (snake_case)"""
user_name = "Alice"
user_age = 25
print(user_name, user_age)  # Output: Alice 25

"""2. Constant Naming (uppercase)"""
PI = 3.14159
GRAVITY = 9.8
print(PI, GRAVITY)  # Output: 3.14159 9.8


"""3. Function Naming (snake_case)"""

def calculate_area(radius):
    return PI * radius ** 2

print(calculate_area(5))  # Output: 78.53975

"""4. Class Naming (CamelCase)"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

dog = Animal("Buddy")
dog.speak()  # Output: Buddy makes a sound.