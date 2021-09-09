from Dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur("ringo", 10)
        dino2 = Dinosaur("george", 9)
        dino3 = Dinosaur("john", 10)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
