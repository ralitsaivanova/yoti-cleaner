
from room import Surface
from vacuum_cleaner import Cleaner

if __name__=="__main__":

    surface = Surface(
        5, 5,
        [[1, 0],
        [2, 2],
        [2, 3]]
    )

    cleaner = Cleaner(
        1, 2, surface
    )

    print(cleaner.clean_surface("NNESEESWNWW"))

