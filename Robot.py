from Weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon("laser")
        # self.weaponslist = []
        # self.add_weapon_to_robot()

    # def add_weapon_to_robot(self):
        #weapon1 = Weapon("laser")
        #weapon2 = Weapon("cluster bomb")
        #weapon3 = Weapon("heat ray")

       # self.weaponslist.append(weapon1)
        # self.weaponslist.append(weapon2)
        # self.weaponslist.append(weapon3)

    def attack(self, dinosaur):
        pass
        # createa function here for robot to attack dino
        # function to lower health score after an attack
