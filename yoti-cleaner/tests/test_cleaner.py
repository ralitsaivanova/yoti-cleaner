import pytest

from app.vacuum_cleaner import VacuumCleaner
from app.room import Floor

class TestCleaner:

    @pytest.fixture()
    def floor(self):
        dirty_patches = [
            [1, 0],
            [2, 2],
            [2, 3]
        ]
        return Floor(5, 5, dirty_patches)

    @pytest.fixture()
    def cleaner(self, floor):
        return VacuumCleaner(1, 2, floor) 

    def test_move_north(self, cleaner):
        cleaner.move_north()
        assert cleaner.get_current_position() == [1, 3]

    def test_move_north_outofbounds(self, cleaner):
        cleaner.set_current_position(0, 4)
        cleaner.move_north()
        assert cleaner.get_current_position() == [0, 4]

    def test_move_south(self, cleaner):
        cleaner.move_south()
        assert cleaner.get_current_position() == [1, 1]

    def test_move_south_outofbounds(self, cleaner):
        cleaner.set_current_position(1, 0)
        cleaner.move_south()
        assert cleaner.get_current_position() == [1, 0]

    def test_move_east(self, cleaner):
        cleaner.move_east()
        assert cleaner.get_current_position() == [2, 2]

    def test_move_east_outofbounds(self, cleaner):
        cleaner.set_current_position(4, 0)
        cleaner.move_east()
        assert cleaner.get_current_position() == [4, 0]

    def test_move_west(self, cleaner):
        cleaner.move_west()
        assert cleaner.get_current_position() == [0, 2]

    def test_move_west_outofbounds(self, cleaner):
        cleaner.set_current_position(0, 4)
        cleaner.move_west()
        assert cleaner.get_current_position() == [0, 4]

    def test_clean_floor(self, cleaner):
        result = cleaner.clean_floor("NNESEESWNWW")

        assert result == {
          "coords" : [1, 3],
          "patches" : 1
        }

    def test_clean_floor_with_many_outofbounds(self, cleaner):
        cleaner.set_current_position(0, 0)
        result = cleaner.clean_floor("SWNNNNNNNNNNNWWWWWWWE")

        assert result == {
          "coords" : [1, 4],
          "patches" : 0
        }
