class Lazer:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.lazer = Lazer()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f"""I have many attachments:
    My lazer, to {self.lazer.does()},
    My claw, to {self.claw.does()},
    My smart phone to {self.smartphone.does()}"""


robbie = Robot()
print(robbie.does())
