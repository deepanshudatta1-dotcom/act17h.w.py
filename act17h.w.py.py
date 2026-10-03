class Robot:
    # Constructor to initialize the robot's name
    def __init__(self, name):
        self.name = name

    # Method for the robot to introduce itself
    def introduce(self):
        print(f"Hello! I am {self.name}, your friendly robot.")


# Creating objects (instances) for Tom and Jerry
robot1 = Robot("Tom")
robot2 = Robot("Jerry")

# Calling the introduce method for both robots
robot1.introduce()
robot2.introduce()