from services.smile import Smile


# gustavomaedo
class App:
    smile = Smile()

    def init_app(self):
        self.smile.set_size(16, 16)
        self.smile.set_icon("▓")
        self.smile.set_empty_icon(".")
        self.add_coordinates()
        self.smile.create_image()
        self.smile.print_image()

    def add_coordinates(self):
        # position
        x = 4
        y = 4
        # y = 0
        self.smile.add_coordinate(x + 2, y + 0)
        self.smile.add_coordinate(x + 3, y + 0)
        self.smile.add_coordinate(x + 4, y + 0)
        self.smile.add_coordinate(x + 5, y + 0)

        # y = 1
        self.smile.add_coordinate(x + 1, y + 1)
        self.smile.add_coordinate(x + 6, y + 1)

        # y = 2
        self.smile.add_coordinate(x + 0, y + 2)
        self.smile.add_coordinate(x + 2, y + 2)
        self.smile.add_coordinate(x + 5, y + 2)
        self.smile.add_coordinate(x + 7, y + 2)

        # y = 3
        self.smile.add_coordinate(x + 0, y + 3)
        self.smile.add_coordinate(x + 7, y + 3)

        # y = 4
        self.smile.add_coordinate(x + 0, y + 4)
        self.smile.add_coordinate(x + 2, y + 4)
        self.smile.add_coordinate(x + 5, y + 4)
        self.smile.add_coordinate(x + 7, y + 4)

        # y = 5
        self.smile.add_coordinate(x + 0, y + 5)
        self.smile.add_coordinate(x + 3, y + 5)
        self.smile.add_coordinate(x + 4, y + 5)
        self.smile.add_coordinate(x + 7, y + 5)

        # y = 6
        self.smile.add_coordinate(x + 1, y + 6)
        self.smile.add_coordinate(x + 6, y + 6)

        # y = 7
        self.smile.add_coordinate(x + 2, y + 7)
        self.smile.add_coordinate(x + 3, y + 7)
        self.smile.add_coordinate(x + 4, y + 7)
        self.smile.add_coordinate(x + 5, y + 7)
