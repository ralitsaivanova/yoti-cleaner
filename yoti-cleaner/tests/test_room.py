import pytest

from app.room import Floor

class TestFloor:

    @pytest.fixture()
    def floor(self):
        dirty_patches = [
            [1, 2],
            [3, 4],
            [2, 3]
        ]
        return Floor(5, 5, None)

    @pytest.mark.parametrize("x, y", [(0, 4), (1, 4), (2, 0), (1, 1)])
    def test_in_bounds(self, floor, x, y):
        assert floor.in_bounds(x, y)

    @pytest.mark.parametrize("x, y", [(0, 5), (7, 4), (2, 6), (8, 1)])
    def test_out_of_bounds(self, floor, x, y):
         assert not floor.in_bounds(x, y)
