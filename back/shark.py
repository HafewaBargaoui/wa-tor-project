from fish import Fish
import constants as cs

class Shark(Fish):

    def __init__(self, pos_x: int, pos_y: int) -> None:
        """Shark constructor

        Args:
            pos_x (int): x position in the grid
            pos_y (int): y position in the grid
        """
        super().__init__(pos_x, pos_y)
        self.energy = cs.INI_SHARK_STARTING_ENERGY

    def eat(self) -> None:
        """ Eat method
            Gives energy to the shark 
        """
        # adds cs.INI_SHARK_EATING_REGEN to the shark's energy
        self.energy += cs.INI_SHARK_EATING_REGEN
        # shark's energy cannot exceed the shark's max energy
        if self.energy > cs.INI_SHARK_STARTING_ENERGY:
            self.energy = cs.INI_SHARK_STARTING_ENERGY

    def can_repro(self) -> bool:
        """ Method that indicates if the shark can reproduce

        Returns:
            bool: shark can reproduce this cycle
        """
        return True if self.repro_time >= cs.INI_SHARK_TIME_TO_REPRODUCE else False

    def can_starve(self) -> bool:
        """ Method that indicates if the shark starves and dies this cycle

        Returns:
            bool: shark dies this cycle
        """
        return True if self.energy <= 0 else False
    
    def __str__(self) -> str:
        """ Method to print a shark's informations

        Returns:
            str: shark's informations
        """
        return f'shark {self.pos_y}, {self.pos_x}, {self.repro_time}, {self.energy}'

