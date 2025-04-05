class Father:
    def __init__(self, name, **kwargs):
        print("Father's init called")
        self.name = name
        super().__init__(**kwargs)  

class Mother:
    def __init__(self, eye_color, **kwargs):
        print("Mother's init called")
        self.eye_color = eye_color
        super().__init__(**kwargs)  

class Child(Father, Mother):
    def __init__(self, name, eye_color):
        print("Child's init called")
        # Use super() to call Father's __init__ and Mother's __init__ in the correct order
        super().__init__(name=name, eye_color=eye_color)

    def display_info(self):
        print(f"Name: {self.name}, Eye Color: {self.eye_color}")

# Create an instance of Child
child = Child(name="John", eye_color="Blue")

# Display child's information
child.display_info()
