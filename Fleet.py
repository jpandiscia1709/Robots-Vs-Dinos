from Robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("larry")
        robot2 = Robot("curly")
        robot3 = Robot("moe")

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
