# gustavomaedo
class Smile:
    is_set = False
    height = 0
    width = 0
    icon = " X "
    no_icon = "   "
    coordinates = [{}]
    image = []

    def set_size(self, height, width):
        if not self.is_set:
            print("aaassr")
            self.height = height
            self.width = width
            self.is_set = True

    def set_icon(self, icon):
        if self.is_set:
            self.icon = " "+icon+" "

    def set_empty_icon(self, icon):
        if self.is_set:
            self.no_icon = " "+icon+" "

    def clear_coordinates(self):
        if self.is_set:
            self.coordinates.clear()

    def add_coordinate(self, x, y):
        if self.is_set:
            coordinate = {
                "x": x,
                "y": y
            }
            self.coordinates.append(coordinate)

    def create_image(self):
        if self.is_set:
            for i in range(self.height):
                self.image.append(self.get_row(i))

    def print_image(self):
        if self.is_set:
            for row in self.image:
                print(row)

    def get_row(self, index):
        icons = []
        row = ""
        for value in self.coordinates:
            x = value.get("x")
            y = value.get("y")
            if y == index:
                icons.append(x)
        for i in range(self.width):
            content = self.no_icon
            if i in icons:
                content = self.icon
            row = row + content
        return row
