class Boat:

    def __init__(self, pos_x: int, pos_y: int) -> None:
        """ Fish Constructor

        Args:
            pos_x (int): x position in the grid
            pos_y (int): y position in the grid
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

        #self.repro_time = random.randint(0, cs.INI_FISH_TIME_TO_REPRODUCE)

    # def can_repro(self) -> bool:
    #     """ Method that indicates if the fish can reproduce

    #     Returns:
    #         bool: fish can reproduce this cycle
    #     """
    #     return True if self.repro_time >= cs.INI_FISH_TIME_TO_REPRODUCE else False

    def __str__(self) -> str:
        """ Method to print a fish's informations

        Returns:
            str: fish's informations
        """
        return f'the fish {self.pos_y}, {self.pos_x}'