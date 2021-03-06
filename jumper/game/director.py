from game.console import Console
from game.jumper import Jumper
from game.word import Word
import time

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
        self.current_guess = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
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
        #display_answer = self.word.answer
        #self.console.write(display_answer)
        display_board = self.word.board
        self.console.write(display_board)
        print()
        display_parachute = self.jumper.draw_parachute(self.lives)
        self.console.picture(display_parachute)
        display_jumper = self.jumper.draw_jumper(self.lives)
        self.console.picture(display_jumper)
        trash = self.word.wrong_guesses
        self.console.write(trash)
        print()
        letter = self.console.read_letter("Guess a letter [a-z]: ")
        self.word.update_word(letter)
        self.current_guess = letter
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the word based on the player's guesses.

        Args:
            self (Director): An instance of Director.
        """
        if self.word.wrong_letter(self.current_guess):
            self.lives -= 1
        #print(self.lives)
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the wrong guesses are displayed and win/lose
        events.

        Args:
            self (Director): An instance of Director.
        """
        self.keep_playing = self.lives > 0 and self.word.answer != self.word.board
        if self.lives == 0:
            display_parachute = self.jumper.draw_parachute(self.lives)
            self.console.picture(display_parachute)
            display_jumper = self.jumper.draw_jumper(self.lives)
            self.console.picture(display_jumper)
            self.console.print_slow("You, ")
            time.sleep(0.3)
            self.console.print_slow("you killed him. ")
            time.sleep(0.3)
            self.console.print_slow("Sweet motherboard, ")
            time.sleep(0.3)
            self.console.print_slow("there are 1s and 0s everywhere!!!")
        if self.word.answer == self.word.board:
            display_board = self.word.board
            self.console.write(display_board)
            display_jumper = self.jumper.draw_winner()
            self.console.picture(display_jumper)
            self.console.print_fast("He's alive! ")
            time.sleep(0.3)
            self.console.print_fast("All hail the word nerd! ")
            time.sleep(0.3)
            self.console.print_fast("Protector of skydiving stick figures!")
