class Word:
    """A code template for the correct word and the blanks. The responsibility
    of this class of objects is to test the inputs of the user and update
    the blanks accordingly.
    
    Stereotype:
        Information Holder

    Attributes:
        answer (list of strings): The location of each correct letter.
        board (list of strings): The game board holding the blanks and correctly
        guessed letters.
        wrong_guesses (list of strings): The guessed letters not found in answer.

    """
    def __init__(self):
        """The class constructor.

        Args:
            self.word and instance of word.
        """
        self.answer = ["j", "a", "z", "z"]
        self.board = ["_", "_", "_", "_"]
        self.wrong_guesses = []

    def update_word(self, letter):
        """Update the input of the user and update the board accordingly.

        Args:
            self (Word): An instance of Word
            letter (char): The input of the user.
        """
        # while letter in self.answer:
        for i in range(self.answer):
            if self.answer == letter:
                self.board[i] = letter