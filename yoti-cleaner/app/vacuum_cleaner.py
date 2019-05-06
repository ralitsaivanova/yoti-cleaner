class VacuumCleaner:

    def __init__(self, coord_x, coord_y, surface):
        if int(coord_x) < 0 or int(coord_y) < 0:
            raise ValueError(
                "Only positive integers are accepted as coordinates")

        self.coord_x = int(coord_x)
        self.coord_y = int(coord_y)
        self.patches_cleaned = 0
        self.surface = surface

    def clean_floor(self, directions):

        for direction in directions:
            if direction.upper() == "N":
                self.move_north()
            elif direction.upper() == "E":
                self.move_east()
            elif direction.upper() == "W":
                self.move_west()
            elif direction.upper() == "S":
                self.move_south()

        return {
          "coords" : self.get_current_position(),
          "patches" : self.patches_cleaned
        }

    def move_north(self):
        temp_coord_y = self.coord_y + 1
        if self.surface.in_bounds(self.coord_x, temp_coord_y):
            self.coord_y = temp_coord_y
            self._clean_patch()

    def move_south(self):
        temp_coord_y = self.coord_y - 1
        if self.surface.in_bounds(self.coord_x, temp_coord_y):
            self.coord_y = temp_coord_y
            self._clean_patch()

    def move_east(self):
        temp_coord_x = self.coord_x + 1
        if self.surface.in_bounds(temp_coord_x, self.coord_y):
            self.coord_x = temp_coord_x
            self._clean_patch()

    def move_west(self):
        temp_coord_x = self.coord_x - 1
        if self.surface.in_bounds(temp_coord_x, self.coord_y):
            self.coord_x = temp_coord_x
            self._clean_patch()

    def _clean_patch(self):
        cleaned_patch = self.surface.remove_dirty_patch(
            self.coord_x, self.coord_y)
        self.patches_cleaned = self.patches_cleaned + cleaned_patch

    def get_patches_cleaned(self):
        return self.patches_cleaned

    def get_current_position(self):
        return [self.coord_x, self.coord_y]

    def set_current_position(self, coord_x, coord_y):
        if int(coord_x) >= 0 or int(coord_y) >= 0:
            self.coord_x = coord_x
            self.coord_y = coord_y
        else:
            raise ValueError(
                "Only positive integers are accepted as coordinates")







