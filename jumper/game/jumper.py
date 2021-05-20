class Jumper:
    """A code template for the display of the parachute and jumper. The responsibility
    of this class of objects is to update the display based on the number of lives 
    remaining.
    
    Stereotype:
        Information Holder

    Attributes:
        answer (list of strings): The location of each correct letter.
        board (list of strings): The game board holding the blanks and correctly
        guessed letters.
        wrong_guesses (list of strings): The guessed letters not found in answer.

    """
    def __init__(self):
        self.parachute = []
        self.jumper = []

    def parachute(self, lives):
        self.parachute[0] = "    ____    "
        self.parachute[1] = "   /____\   "
        self.parachute[2] = "   \    /   "
        self.parachute[3] = "    \  /    "

        if lives == 4:
            return self.parachute[0,1,2,3]

    def jumper(self, lives):
        pass

jumper = Jumper()
print(jumper.parachute(4))