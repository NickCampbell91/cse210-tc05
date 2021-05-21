import sys,time

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as a string.
        """
        return input(prompt)
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(*text)
        
    def picture(self, text_art):
        """Displays the given text art on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text_art (list): The text art to display.
        """
        print(*text_art, sep = "\n")

    def print_slow(self, str):
        """Slow the text to give the impression of speaking. 

        Args: 
            self (Screen): An instance of Screen.
            str (string): The text to display.
        """
        for letter in str:
            sys.stdout.write(letter) #types the letter
            sys.stdout.flush() #clears the internal buffer
            time.sleep(0.1) #creates delay between letters
        #print() #without this everything is printed on the same line

    def print_fast(self, str):
        """Somewhat slow the text to give the impression of speaking. 

        Args: 
            self (Screen): An instance of Screen.
            str (string): The text to display.
        """
        for letter in str:
            sys.stdout.write(letter) #types the letter
            sys.stdout.flush() #clears the internal buffer
            time.sleep(0.04) #creates delay between letters
        #print() #without this everything is printed on the same line