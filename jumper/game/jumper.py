class Jumper:
    """A code template for the display of the parachute and jumper. The responsibility
    of this class of objects is to update the display based on the number of lives 
    remaining.
    
    Stereotype:
        Information Holder

    Attributes:
        parachute (list of strings): The visual representation of the lives remaining.
        board (list of strings): The game board holding the blanks and correctly
        guessed letters.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.parachute = ["", "", "", ""]
        self.jumper = ["", "", "", "", ""]
    
    def draw_parachute(self, lives):
        """Displays the various levels of the parachute depending on the 
        number of lives remaining.

        Args:
            self (Jumper): An instance of Jumper.
            lives (integer): The number of lives remaining.
        """
        if lives > 3:
            self.parachute[0] = "    ____    "
        else:
            self.parachute[0] = ""
        if lives > 2:
            self.parachute[1] = "   /____\   "
        else:
            self.parachute[1] = ""
        if lives > 1:
            self.parachute[2] = "   \    /   "
        else:
            self.parachute[2] = ""
        if lives > 0:
            self.parachute[3] = "    \  /    "
        else:
            self.parachute[3] = ""

        parachute = self.parachute

        return parachute

    def draw_jumper(self, lives):
        """Displays the jumper, alive or not so mmuch, depending on the 
        number of lives remaining.

        Args:
            self (Jumper): An instance of Jumper.
            lives (integer): The number of lives remaining.
        """
        if lives > 0:
            self.jumper[0] = "     o      "
            self.jumper[1] = "    /|\     "
            self.jumper[2] = "    / \     "
            self.jumper[3] = "            "
            self.jumper[4] = "^^^^^^^^^^^^"
        else:
            self.jumper[0] = "            "
            self.jumper[1] = "            "
            self.jumper[2] = "            "
            self.jumper[3] = "            "
            self.jumper[4] = "^^^^>->o^^^^"
        
        jumper = self.jumper

        return jumper
    
    def draw_winner(self):
        """Displays the jumper safely landed on the ground.

        Args:
            self (Jumper): An instance of Jumper.
        """
        happy_jumper = ["", "", "", "", ""]
        happy_jumper[0] = "            "
        happy_jumper[1] = "            "
        happy_jumper[2] = "    \o/     "
        happy_jumper[3] = "     |      "
        happy_jumper[4] = "^^^^/ \^^^^^"

        return happy_jumper

def test():
    """
    A function only used for testing purposes.
    """
    jumper = Jumper()
    lives = 0
    display = jumper.draw_parachute(lives)
    print(*display, sep = "\n")
    other_display = jumper.draw_jumper(lives)
    print(*other_display, sep = "\n")

#test()