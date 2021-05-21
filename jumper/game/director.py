from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        word (Word): An instance of the class of objects known as Word.
        lives (integer): The number of lives remaining.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.word = Word()
        self.keep_playing = True
        self.lives = 4

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        #print(self.jumper.parachute)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means displaying the game and guessing if the letter is in the word.

        Args:
            self (Director): An instance of Director.
        """
        display_word = self.word.board
        self.console.write(display_word)
        print()
        display_parachute = self.jumper.draw_parachute(self.lives)
        self.console.picture(display_parachute)
        display_jumper = self.jumper.draw_jumper(self.lives)
        self.console.picture(display_jumper)
        print()
        letter = self.console.read_letter("Guess a letter [a-z]: ")
        #self.word.update_word(letter)
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the word based on the player's guesses.

        Args:
            self (Director): An instance of Director.
        """
        if self.word.update_word():
            
            self.lives -= 1

        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the wrong guesses are displayed.

        Args:
            self (Director): An instance of Director.
        """
        trash = self.word.wrong_guesses
        self.console.write(trash)
        self.keep_playing = self.lives > 0
